---
id: learning.zephyr-docs.boards-nxp-imx-rt-multicore.page-5
title: MIMXRT595-EVK
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/mimxrt595_evk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mimxrt595_evk"></a>

# 第5章\_MIMXRT595-EVK

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/mimxrt595_evk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/mimxrt595_evk.jpg](images/mimxrt595_evk.jpg)](images/mimxrt595_evk.jpg)

MIMXRT595-EVK

名称（Name）：

`mimxrt595_evk`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)、[xtensa](https://docs.zephyrproject.org/latest/boards/index.html#arch=xtensa)

片上系统（SoC）：

[mimxrt595s](https://docs.zephyrproject.org/latest/boards/index.html#soc=mimxrt595s)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mimxrt595_evk/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

i.MX RT500跨界MCU属于边缘计算系列，将图形引擎、精简的Cadence Tensilica Fusion F1数字信号处理器（DSP）及新一代Arm Cortex-M33结合，用于低功耗人机界面（HMI）应用。它以兼顾安全及功耗的嵌入式处理器支持显示类应用。

i.MX RT500提供最高5 MB片上SRAM，以及多个访问片外闪存的高带宽接口，包括带即时解密引擎（On-the-fly Decryption Engine）的八线／四线SPI接口。

<a id="hardware"></a>

## 硬件（Hardware）


- MIMXRT595SFFOC Cortex-M33处理器，275 MHz，带Cadence Tensilica Fusion F1 DSP
- 板载高速USB Link2调试探针，采用CMSIS-DAP协议，仅支持Cortex-M33调试
- USB 2.0高速主机及设备接口，使用Micro-USB连接器及外部晶体
- 通过FlexSPI连接八线／四线闪存及伪静态RAM（pSRAM）等外部存储器
- 5 MB系统SRAM
- 全尺寸SD卡槽，支持SDIO
- 板载eMMC芯片
- 板载NXP PCA9420UK电源管理芯片（PMIC），5 V输入，提供1.2 V、1.8 V及3.3 V电源
- 用户LED
- 复位及用户按键
- MIPI-DSI连接器
- Arduino信号单排排针及mikroBUS连接器
- FlexIO连接器，用于MikroElektronika TFT Proto 5英寸电容触摸显示屏
- NXP FXOS8700CQ组合运动传感器，包含加速度计及磁力计
- 立体声音频编解码器，带线路输入、线路输出及麦克风
- Pmod／主机扩展连接器
- NXP TFA9896数字音频放大器
- 通过12引脚排针最多支持8个板外数字麦克风
- 两个板载数字麦克风

MIMXRT595 SoC及MIMXRT595-EVK开发板的更多信息见以下资料：


- [i.MX RT595 网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt500-crossover-mcu-with-arm-cortex-m33-dsp-and-gpu-cores:i.MX-RT500)
- [i.MX RT595 数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/IMXRT500EC.pdf)
- [i.MX RT595 参考手册（Reference Manual）](https://www.nxp.com/webapp/Download?colCode=IMXRT500RM)
- [MIMXRT595-EVK 网站](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/i-mx-rt595-evaluation-kit:MIMXRT595-EVK)
- [MIMXRT595-EVK用户指南（User Guide）](https://www.nxp.com/webapp/Download?colCode=MIMXRT595EVKHUG)
- [MIMXRT595-EVK原理图（Schematics）](https://www.nxp.com/downloads/en/schematics/MIMXRT595-EVK-DESIGN-FILES.zip)
- [MIMXRT595-EVK调试固件（Debug Firmware）](https://www.nxp.com/docs/en/application-note/AN13206.pdf)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

NXP将MIMXRT595-EVK视为i.MX RT5xx系列功能覆盖更广的开发板，并优先在此板落实Zephyr完整平台支持及新功能，以服务整个RT5xx系列。另一块相似开发板[MIMXRT685-EVK](P007_MIMXRT685-EVK.md#mimxrt685_evk)可能已有可复用于mimxrt595_evk的额外功能。

`mimxrt595_evk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mimxrt595_evk-hw-features"></a>

<a id="mimxrt595_evk-mimxrt595_evk/mimxrt595s/cm33-hw-features-section"></a>

#### `mimxrt595_evk/mimxrt595s/cm33`目标（Target）

<a id="mimxrt595_evk-mimxrt595_evk/mimxrt595s/cm33-hw-features-panel"></a>

<a id="mimxrt595_evk-mimxrt595_evk/mimxrt595s/cm33-hw-features-memory"></a>

该开发板目标的片上存储容量：3 MiB RAM、64 MiB Flash。

<a id="mimxrt595_evk-mimxrt595_evk/mimxrt595s/cm33-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L29">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L648">已启用：1</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>LPC Flexcomm节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L320">已禁用：9</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P015_nxp_lpc-flexcomm.md#std-dtcompatible-nxp-lpc-flexcomm"><code>nxp,lpc-flexcomm</code></a></td>
</tr>
<tr>
<td rowspan="2">音频（Audio）</td>
<td>片上（On-Chip）</td>
<td>NXP数字麦克风接口（DMIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L511">已启用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P013_nxp_dmic.md#std-dtcompatible-nxp-dmic"><code>nxp,dmic</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>WM8904音频编解码器（Audio Codec）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L524">已启用：1</a>）</td>
<td><a href="../audio_stm32_ti_wolfson_binding_reference/P011_wolfson_wm8904.md#std-dtcompatible-wolfson-wm8904"><code>wolfson,wm8904</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L133">已启用：2</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟监测（Clock Monitor）</td>
<td>片上（On-Chip）</td>
<td>NXP BASIC频率测量（FREQME / fmeas）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L164">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P003_nxp_fmeas.md#std-dtcompatible-nxp-fmeas"><code>nxp,fmeas</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>使用NXP LPC RTC高分辨率计数器（High Resolution Counter）的驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L583">已禁用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P010_nxp_lpc-rtc-highres.md#std-dtcompatible-nxp-lpc-rtc-highres"><code>nxp,lpc-rtc-highres</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX标准定时器／计数器（Standard Timer/Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L671">已启用：5</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer"><code>nxp,lpc-ctimer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器（Multirate Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L766">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P015_nxp_mrt.md#std-dtcompatible-nxp-mrt"><code>nxp,mrt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L777">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L783">已禁用：3</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P014_nxp_mrt-channel.md#std-dtcompatible-nxp-mrt-channel"><code>nxp,mrt-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L338">已启用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P007_nxp_lpc-crc.md#std-dtcompatible-nxp-lpc-crc"><code>nxp,lpc-crc</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>片上（On-Chip）</td>
<td>NXP DCNano LCD接口（LCDIF）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L444">已禁用：1</a>）</td>
<td><a href="../display_ilitek_matrix_nxp_binding_reference/P017_nxp_dcnano-lcdif.md#std-dtcompatible-nxp-dcnano-lcdif"><code>nxp,dcnano-lcdif</code></a></td>
</tr>
<tr>
<td rowspan="2">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L487">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L499">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P003_nxp_lpc-dma.md#std-dtcompatible-nxp-lpc-dma"><code>nxp,lpc-dma</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP SmartDMA控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L662">已启用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P007_nxp_smartdma.md#std-dtcompatible-nxp-smartdma"><code>nxp,smartdma</code></a></td>
</tr>
<tr>
<td rowspan="1">数字信号处理（DSP）</td>
<td>片上（On-Chip）</td>
<td>NXP PowerQuad数字信号处理（DSP）协处理器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L803">已禁用：1</a>）</td>
<td><a href="../sound_haptic_binding_reference/P004_nxp_powerquad.md#std-dtcompatible-nxp-powerquad"><code>nxp,powerquad</code></a></td>
</tr>
<tr>
<td rowspan="3">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>LPC通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L232">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P006_nxp_lpc-gpio.md#std-dtcompatible-nxp-lpc-gpio"><code>nxp,lpc-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>LPC GPIO端口设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L238">已启用：7</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P005_nxp_lpc-gpio-port.md#std-dtcompatible-nxp-lpc-gpio-port"><code>nxp,lpc-gpio-port</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Arduino Uno R3排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L82">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P023_arduino-header-r3.md#std-dtcompatible-arduino-header-r3"><code>arduino-header-r3</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC 128位唯一标识符（Unique Identifier）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L227">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P009_nxp_lpc-uid.md#std-dtcompatible-nxp-lpc-uid"><code>nxp,lpc-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>LPC I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L345">已启用：2</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P003_nxp_lpc-i2c.md#std-dtcompatible-nxp-lpc-i2c"><code>nxp,lpc-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>LPC I2S音频总线节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L311">已禁用：2</a>）</td>
<td><a href="../i2s_binding_reference/P012_nxp_lpc-i2s.md#std-dtcompatible-nxp-lpc-i2s"><code>nxp,lpc-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L744">已启用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L47">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP引脚中断及模式匹配引擎（PINT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L290">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L63">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>用作Zephyr邮箱（MBOX）的NXP i.MX消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L757">已启用：1</a>）</td>
<td><a href="../intercore_reference/P047_NXPiMX消息单元邮箱绑定.md#dtbinding-nxp-mbox-imx-mu"><code>nxp,mbox-imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示串行接口（MIPI-DSI）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX MIPI DSI双通道显示串行接口（2L）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L731">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P014_nxp_mipi-dsi-2l.md#std-dtcompatible-nxp-mipi-dsi-2l"><code>nxp,mipi-dsi-2l</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L37">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="3">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>NXP FlexSPI MX25UM51345G闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L423">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P021_nxp_imx-flexspi-mx25um51345g.md#std-dtcompatible-nxp-imx-flexspi-mx25um51345g"><code>nxp,imx-flexspi-mx25um51345g</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L436">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>连接NXP FlexSPI总线的AP Memory APS6408L伪静态RAM（pSRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L494">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P017_nxp_imx-flexspi-aps6408l.md#std-dtcompatible-nxp-imx-flexspi-aps6408l"><code>nxp,imx-flexspi-aps6408l</code></a></td>
</tr>
<tr>
<td rowspan="1">多路复用器（MUX）</td>
<td>片上（On-Chip）</td>
<td>NXP输入复用器（INPUTMUX）外设绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L156">已禁用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux"><code>nxp,inputmux</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>LPC I/O引脚配置（IOCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L140">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P007_nxp_lpc-iocon.md#std-dtcompatible-nxp-lpc-iocon"><code>nxp,lpc-iocon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>RT600／RT500引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L144">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P018_nxp_rt-iocon-pinctrl.md#std-dtcompatible-nxp-rt-iocon-pinctrl"><code>nxp,rt-iocon-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>通过PDCFG寄存器实现NXP电源管理的属性（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L53">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P015_nxp_pdcfg-power.md#std-dtcompatible-nxp-pdcfg-power"><code>nxp,pdcfg-power</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>NXP状态可配置定时器（SCTimer）脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L596">已启用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P012_nxp_sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm"><code>nxp,sctimer-pwm</code></a></td>
</tr>
<tr>
<td rowspan="2">稳压器（Regulator）</td>
<td>板载（On-Board）</td>
<td>NXP PCA9420电源管理芯片（PMIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L255">已启用：1</a>）</td>
<td><a href="../hardware/P668_PCA9420稳压器绑定.md#dtbinding-nxp-pca9420"><code>nxp,pca9420</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>固定电压稳压器（Fixed Voltage Regulators）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L133">已启用：1</a>）</td>
<td><a href="../hardware/P635_固定稳压器设备树绑定.md#dtbinding-regulator-fixed"><code>regulator-fixed</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP RSTCTL外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L215">已启用：2</a>）</td>
<td><a href="../reset_controller_binding_reference/P011_nxp_rstctl.md#std-dtcompatible-nxp-rstctl"><code>nxp,rstctl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Kinetis真随机数发生器（TRNG / True Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L589">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P020_nxp_kinetis-trng.md#std-dtcompatible-nxp-kinetis-trng"><code>nxp,kinetis-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L577">已启用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P013_nxp_lpc-rtc.md#std-dtcompatible-nxp-lpc-rtc"><code>nxp,lpc-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L624">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L636">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P014_nxp_imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc"><code>nxp,imx-usdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>FXOS8700六轴加速度计／磁力计传感器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L189">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P052_nxp_fxos8700.md#std-dtcompatible-nxp-fxos8700"><code>nxp,fxos8700</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC通用同步异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L302">已启用：2</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P014_nxp_lpc-usart.md#std-dtcompatible-nxp-lpc-usart"><code>nxp,lpc-usart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L123">已启用：2</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP LPC串行外设接口（SPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L476">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L465">已禁用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P003_nxp_lpc-spi.md#std-dtcompatible-nxp-lpc-spi"><code>nxp,lpc-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L86">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>i.MX RT5xx／6xx上的NXP操作系统定时器（OS Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L569">已启用：1</a>）</td>
<td><a href="../microchip_nordic_nxp_realtek_timer_binding_reference/P008_nxp_os-timer.md#std-dtcompatible-nxp-os-timer"><code>nxp,os-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ARMv8-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21">已禁用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P007_ARMv8_M_SysTick.md#std-dtcompatible-arm-armv8m-systick"><code>arm,armv8m-systick</code></a></td>
</tr>
<tr>
<td rowspan="2">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>NXP LPCIP3511 USB设备模式（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L451">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P008_nxp_lpcip3511.md#std-dtcompatible-nxp-lpcip3511"><code>nxp,lpcip3511</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L459">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P013_nxp_usbphy.md#std-dtcompatible-nxp-usbphy"><code>nxp,usbphy</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>LPC窗口看门狗定时器（Windowed Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L606">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt5xx/nxp_rt5xx_common.dtsi?plain=1#L615">已禁用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P011_nxp_lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt"><code>nxp,lpc-wwdt</code></a></td>
</tr>
</table>

<a id="shields-for-supported-features"></a>

### 支持相应功能的扩展板（Shields）

上表部分功能使用Zephyr扩展板测试，以下扩展板已在此板上测试：


- NXP RK055HDMIPI4M、RK055HDMIPI4MA0及G1120B0MIPI显示屏：支持MIPI-DSI显示接口。（[NXP RK055HDMIPI4M MIPI显示屏](https://docs.zephyrproject.org/latest/boards/shields/rk055hdmipi4m/doc/index.html#rk055hdmipi4m)；[NXP RK055HDMIPI4MA0 MIPI显示屏](https://docs.zephyrproject.org/latest/boards/shields/rk055hdmipi4ma0/doc/index.html#rk055hdmipi4ma0)；[NXP G1120B0MIPI MIPI显示屏](https://docs.zephyrproject.org/latest/boards/shields/g1120b0mipi/doc/index.html#g1120b0mipi)）

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

MIMXRT595 SoC提供IOCON寄存器，用于配置引脚功能。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PIO0_2</td>
<td>USART0</td>
<td>USART接收（RX）</td>
</tr>
<tr>
<td>PIO0_1</td>
<td>USART0</td>
<td>USART发送（TX）</td>
</tr>
<tr>
<td>PIO0_14</td>
<td>通用输入输出（GPIO）</td>
<td>绿色LED（GREEN LED）</td>
</tr>
<tr>
<td>PIO0_25</td>
<td>通用输入输出（GPIO）</td>
<td>SW0</td>
</tr>
<tr>
<td>PIO0_10</td>
<td>通用输入输出（GPIO）</td>
<td>SW1</td>
</tr>
<tr>
<td>PIO4_30</td>
<td>USART12</td>
<td>USART发送（TX）</td>
</tr>
<tr>
<td>PIO4_31</td>
<td>USART12</td>
<td>USART接收（RX）</td>
</tr>
<tr>
<td>PIO0_29</td>
<td>集成电路间总线（I2C）</td>
<td>I2C串行时钟（SCL）</td>
</tr>
<tr>
<td>PIO0_30</td>
<td>集成电路间总线（I2C）</td>
<td>I2C串行数据（SDA）</td>
</tr>
<tr>
<td>PIO0_22</td>
<td>通用输入输出（GPIO）</td>
<td>FXOS8700触发（TRIGGER）</td>
</tr>
<tr>
<td>PIO1_5</td>
<td>串行外设接口（SPI）</td>
<td>SPI主机输出从机输入（MOSI）</td>
</tr>
<tr>
<td>PIO1_4</td>
<td>串行外设接口（SPI）</td>
<td>SPI主机输入从机输出（MISO）</td>
</tr>
<tr>
<td>PIO1_3</td>
<td>串行外设接口（SPI）</td>
<td>SPI串行时钟（SCK）</td>
</tr>
<tr>
<td>PIO1_6</td>
<td>串行外设接口（SPI）</td>
<td>SPI从设备选择（SSEL）</td>
</tr>
<tr>
<td>PIO0_5</td>
<td>SCT0</td>
<td>SCT0通用输入0（GPI0）</td>
</tr>
<tr>
<td>PIO0_6</td>
<td>SCT0</td>
<td>SCT0通用输入1（GPI1）</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

MIMXRT595 EVK配置为使用操作系统事件定时器（OS Event Timer）作为系统时钟源。

<a id="serial-port"></a>

### 串口（Serial Port）

MIMXRT595 SoC有13路FLEXCOMM串行通信接口，一路配置为控制台USART，其余未使用。

<a id="fusion-f1-dsp-core"></a>

### Fusion F1 DSP核

以F1 SoC为目标可为RT500 DSP核构建Zephyr应用。Zephyr SDK包含支持该DSP核的Xtensa工具链。构建Hello World示例的方法如下：

```text
$ west build -b mimxrt595_evk/mimxrt595s/f1 samples/hello_world
```

DSP固件调试的详细说明见《[EVK-MIMXRT595 Xplorer快速入门](https://www.nxp.com/docs/en/supporting-information/GSXEVKMIMXRT595.pdf)》（Getting Started with Xplorer for EVK-MIMXRT595）。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`mimxrt595_evk`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-linkserver">linkserver</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td></td>
<td></td>
<td>✅</td>
</tr>
</table>

按通常方式构建并烧录应用，详见“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）与“运行应用”（[Run an Application](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）。

<a id="configuring-a-debug-probe"></a>

### 配置调试探针（Configuring a Debug Probe）

烧录及调试都使用调试探针，此板默认使用LPC-Link2。

<a id="tab-0-TFBDTGluazIgSkxpbmsgT25ib2FyZA=="></a>

<a id="tab-0-SkxpbmsgRXh0ZXJuYWw="></a>

<a id="tab-0-TGlua3NlcnZlcg=="></a>

<a id="panel-0-TFBDTGluazIgSkxpbmsgT25ib2FyZA=="></a>

**板载LPC-Link2 J-Link**


1. 安装J-Link调试主机工具（Debug Host Tools），并确保工具位于搜索路径中。（[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)）
2. 为把SWD信号连接到板载调试电路，需安装JP17、JP18及JP19，原文说明这些跳线默认安装。
3. 按LPC-Link2 J-Link板载调试探针说明写入J-Link固件，并确保使用此板的最新固件。（[LPC-Link2 J-Link板载调试探针（Onboard Debug Probe）](../debugging/P003_调试探针.md#lpclink2-jlink-onboard-debug-probe)）

<a id="panel-0-SkxpbmsgRXh0ZXJuYWw="></a>

**外部J-Link**


1. 安装J-Link调试主机工具（Debug Host Tools），并确保工具位于搜索路径中。（[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)）
2. 为从板载调试电路断开SWD信号，移除J17、J18及J19。原文此处写J，前文写JP，均保留；这些跳线原文说明默认安装。
3. 将J-Link探针连接到J2的10引脚排针。

更多信息见“外部J-Link调试探针”（[J-Link External Debug Probe](https://docs.zephyrproject.org/latest/develop/flash_debug/probes.html#jlink-external-debug-probe)）。

<a id="panel-0-TGlua3NlcnZlcg=="></a>

**Linkserver**


1. 安装LinkServer调试主机工具，并确保位于搜索路径中。（[LinkServer调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#linkserver-debug-host-tools)）
2. 更新调试固件的方法见“MIMXRT595-EVK调试固件”。

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

用USB线缆将PC连接J40，在所选串口终端（如minicom、PuTTY）中使用以下设置：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing"></a>

### 烧录（Flashing）

以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例，默认使用[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)。

```text
# From the root of the zephyr repository
west build -b mimxrt595_evk/mimxrt595s/cm33 samples/hello_world
west flash
```

打开串口终端，复位开发板（按下RESET按键），应能在终端中看到以下消息：

```text
*** Booting Zephyr OS v2.7 ***
Hello World! mimxrt595_evk
```

<a id="debugging"></a>

### 调试（Debugging）

以下以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例，默认使用[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)。

```text
# From the root of the zephyr repository
west build -b mimxrt595_evk/mimxrt595s/cm33 samples/hello_world
west debug
```

打开串口终端，在调试器中单步运行应用，应能在终端中看到以下消息：

```text
*** Booting Zephyr OS v2.7 ***
Hello World! mimxrt595_evk
```

<a id="troubleshooting"></a>

### 故障排查（Troubleshooting）

若调试探针出现以下连接错误，可能是闪存中的镜像干扰了调试连接。

```text
Remote debugging using :2331
Remote communication error.  Target disconnected.: Connection reset by peer.
"monitor" command not supported by this target.
"monitor" command not supported by this target.
You can't do that when your target is `exec'
(gdb) Could not connect to target.
Please check power, connection and settings.
```

可按以下步骤擦除并重新编程闪存来恢复：


1. 将SW7拨码设为ON-ON-ON，阻止从闪存启动。
2. 按SW3复位。
3. 使用已知可工作的Zephyr应用，例如Hello World，再次运行west debug或west flash。
4. 将SW5拨码设为OFF-OFF-ON，从闪存启动。原文此处为SW5，前一步为SW7。
5. 按SW3复位。

<a id="support-resources-for-zephyr"></a>

### Zephyr支持资源（Support Resources）


- [NXP开发板支持状态（Board Support Status）](https://github.com/nxp-zephyr/nxp-zsdk/blob/main/doc/releases/Board-Support-Status.md)
- [NXP Zephyr下游软件开发工具包（Downstream SDK）](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code文档](https://mcuxpresso.nxp.com/mcux-vscode)及[Zephyr实验指南](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)
- [NXP Zephyr知识中心（Knowledge Hub）](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- NXP Zephyr主页，包含培训资源（[NXP的Zephyr专题页面](https://nxp.com/zephyr)）
- [NXP Zephyr支持社区论坛（Support Community）](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## 译注

板载Link2仅调试Cortex-M33，Fusion F1使用独立DSP工具链与调试流程。原文SWD跳线先写JP17—JP19、后写J17—J19；恢复启动步骤又分别写SW7与SW5，均标注保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [i-mx-rt595-evaluation-kit:MIMXRT595-EVK](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/i-mx-rt595-evaluation-kit:MIMXRT595-EVK)：HTTP Error 404: Not Found。
- [AN13206.pdf](https://www.nxp.com/docs/en/application-note/AN13206.pdf)：HTTP Error 404: Not Found。
- [IMXRT500EC.pdf](https://www.nxp.com/docs/en/data-sheet/IMXRT500EC.pdf)：HTTP Error 404: Not Found。
- [GSXEVKMIMXRT595.pdf](https://www.nxp.com/docs/en/supporting-information/GSXEVKMIMXRT595.pdf)：HTTP Error 404: Not Found。
- [MIMXRT595-EVK-DESIGN-FILES.zip](https://www.nxp.com/downloads/en/schematics/MIMXRT595-EVK-DESIGN-FILES.zip)：HTTP Error 404: Not Found。
- [i-mx-rt500-crossover-mcu-with-arm-cortex-m33-dsp-and-gpu-cores:i.MX-RT500](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt500-crossover-mcu-with-arm-cortex-m33-dsp-and-gpu-cores:i.MX-RT500)：HTTP Error 404: Not Found。
- [Download?colCode=IMXRT500RM](https://www.nxp.com/webapp/Download?colCode=IMXRT500RM)：HTTP Error 404: Not Found。
- [Download?colCode=MIMXRT595EVKHUG](https://www.nxp.com/webapp/Download?colCode=MIMXRT595EVKHUG)：HTTP Error 404: Not Found。

---

[上一章](P004_MIMXRT2660-EVK.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P006_MIMXRT685-AUD-EVK.md)
