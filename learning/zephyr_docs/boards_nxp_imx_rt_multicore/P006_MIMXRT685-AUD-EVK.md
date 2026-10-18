---
id: learning.zephyr-docs.boards-nxp-imx-rt-multicore.page-6
title: MIMXRT685-AUD-EVK
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/nxp/mimxrt685_aud_evk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mimxrt685_aud_evk"></a>

# 第6章\_MIMXRT685-AUD-EVK

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/nxp/mimxrt685_aud_evk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/mimxrt685_aud_evk.webp](images/mimxrt685_aud_evk.webp)](images/mimxrt685_aud_evk.webp)

MIMXRT685-AUD-EVK

名称（Name）：

`mimxrt685_aud_evk`

厂商（Vendor）：

[恩智浦半导体（NXP Semiconductors）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nxp)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[mimxrt685s](https://docs.zephyrproject.org/latest/boards/index.html#soc=mimxrt685s)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mimxrt685_aud_evk/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

i.MX RT600跨界MCU系列面向32位沉浸式音频播放及语音用户界面应用，将高性能Cadence Tensilica HiFi 4音频DSP与新一代Cortex-M33结合，以兼顾安全及功耗的嵌入式处理器支持语音辅助终端节点。

MIMXRT685-AUD-EVK是面向i.MX RT685的音频评估套件，配备CS42448音频编解码器及多种音频接口。

<a id="hardware"></a>

## 硬件（Hardware）


- MIMXRT685SFVKB Cortex-M33处理器，300 MHz、4.5 MB片上SRAM，带Cadence Xtensa HiFi 4 DSP
- 板载高速USB Link2调试探针，采用CMSIS-DAP协议，仅支持Cortex-M33调试
- 高速USB端口，使用Micro-A/B连接器，支持主机或设备功能
- 通过板载调试探针，将i.MX RT685目标的UART、I2C及SPI端口桥接到USB
- 64 MB Macronix Quad SPI闪存，工作电压1.8 V
- NXP PCA9420UK电源管理芯片（PMIC）
- 用户LED
- 复位及用户按键
- CS42448音频编解码器

MIMXRT685 SoC及MIMXRT685-AUD-EVK开发板的更多信息见以下资料：


- [i.MX RT685 网站](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt600-crossover-mcu-with-arm-cortex-m33-and-dsp-cores:i.MX-RT600)
- [i.MX RT685 数据手册（Datasheet）](https://www.nxp.com/docs/en/data-sheet/RT600.pdf)
- [i.MX RT685 参考手册（Reference Manual）](https://www.nxp.com/webapp/Download?colCode=UM11147)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`mimxrt685_aud_evk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="mimxrt685_aud_evk-hw-features"></a>

<a id="mimxrt685_aud_evk-mimxrt685_aud_evk/mimxrt685s/cm33-hw-features-section"></a>

#### `mimxrt685_aud_evk/mimxrt685s/cm33`目标（Target）

<a id="mimxrt685_aud_evk-mimxrt685_aud_evk/mimxrt685s/cm33-hw-features-panel"></a>

<a id="mimxrt685_aud_evk-mimxrt685_aud_evk/mimxrt685s/cm33-hw-features-memory"></a>

该开发板目标的片上存储容量：3 MiB RAM、64 MiB Flash。

<a id="mimxrt685_aud_evk-mimxrt685_aud_evk/mimxrt685s/cm33-hw-features-table"></a>

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
<td>ARM Cortex-M33F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P023_arm_cortex-m33f.md#std-dtcompatible-arm-cortex-m33f"><code>arm,cortex-m33f</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>LPC低功耗模数转换器（LPADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L589">已禁用：1</a>）</td>
<td><a href="../hardware/P851_NXPLPC低功耗ADC绑定.md#dtbinding-nxp-lpc-lpadc"><code>nxp,lpc-lpadc</code></a></td>
</tr>
<tr>
<td rowspan="1">ARM 架构（ARM Architecture）</td>
<td>片上（On-Chip）</td>
<td>LPC Flexcomm节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L314">已禁用：7</a>）</td>
<td><a href="../arm_nordic_nxp_control_binding_reference/P015_nxp_lpc-flexcomm.md#std-dtcompatible-nxp-lpc-flexcomm"><code>nxp,lpc-flexcomm</code></a></td>
</tr>
<tr>
<td rowspan="1">音频（Audio）</td>
<td>片上（On-Chip）</td>
<td>NXP数字麦克风接口（DMIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L444">已禁用：1</a>）</td>
<td><a href="../audio_pdm_codec_binding_reference/P013_nxp_dmic.md#std-dtcompatible-nxp-dmic"><code>nxp,dmic</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>LPC SYSCON及CLKCTL IP节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L138">已启用：2</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P007_nxp_lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon"><code>nxp,lpc-syscon</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟监测（Clock Monitor）</td>
<td>片上（On-Chip）</td>
<td>NXP BASIC频率测量（FREQME / fmeas）模块（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L178">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P003_nxp_fmeas.md#std-dtcompatible-nxp-fmeas"><code>nxp,fmeas</code></a></td>
</tr>
<tr>
<td rowspan="1">比较器（Comparator）</td>
<td>片上（On-Chip）</td>
<td>NXP Kinetis模拟比较器（ACMP / Analog Comparator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L581">已禁用：1</a>）</td>
<td><a href="../hardware/P745_NXPKinetis模拟比较器绑定.md#dtbinding-nxp-kinetis-acmp"><code>nxp,kinetis-acmp</code></a></td>
</tr>
<tr>
<td rowspan="4">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>使用NXP LPC RTC高分辨率计数器（High Resolution Counter）的驱动（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L516">已禁用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P010_nxp_lpc-rtc-highres.md#std-dtcompatible-nxp-lpc-rtc-highres"><code>nxp,lpc-rtc-highres</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP MCUX标准定时器／计数器（Standard Timer/Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L605">已禁用：5</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer"><code>nxp,lpc-ctimer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器（Multirate Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L678">已启用：1</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P015_nxp_mrt.md#std-dtcompatible-nxp-mrt"><code>nxp,mrt</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP多速率定时器通道（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L689">已禁用：4</a>）</td>
<td><a href="../nxp_nuvoton_counter_binding_reference/P014_nxp_mrt-channel.md#std-dtcompatible-nxp-mrt-channel"><code>nxp,mrt-channel</code></a></td>
</tr>
<tr>
<td rowspan="1">循环冗余校验（CRC）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC循环冗余校验（CRC）设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L341">已禁用：1</a>）</td>
<td><a href="../crc_clock_monitor_binding_reference/P007_nxp_lpc-crc.md#std-dtcompatible-nxp-lpc-crc"><code>nxp,lpc-crc</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L426">已禁用：2</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P003_nxp_lpc-dma.md#std-dtcompatible-nxp-lpc-dma"><code>nxp,lpc-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">数字信号处理（DSP）</td>
<td>片上（On-Chip）</td>
<td>NXP PowerQuad数字信号处理（DSP）协处理器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L727">已禁用：1</a>）</td>
<td><a href="../sound_haptic_binding_reference/P004_nxp_powerquad.md#std-dtcompatible-nxp-powerquad"><code>nxp,powerquad</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>LPC通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L242">已启用：1</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P006_nxp_lpc-gpio.md#std-dtcompatible-nxp-lpc-gpio"><code>nxp,lpc-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>LPC GPIO端口设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L248">已启用：6</a>）</td>
<td><a href="../gpio_nxp_expanders_binding_reference/P005_nxp_lpc-gpio-port.md#std-dtcompatible-nxp-lpc-gpio-port"><code>nxp,lpc-gpio-port</code></a></td>
</tr>
<tr>
<td rowspan="1">硬件信息（Hardware Information）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC 128位唯一标识符（Unique Identifier）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L237">已启用：1</a>）</td>
<td><a href="../hwinfo_binding_reference/P009_nxp_lpc-uid.md#std-dtcompatible-nxp-lpc-uid"><code>nxp,lpc-uid</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>LPC I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L384">已禁用：1</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P003_nxp_lpc-i2c.md#std-dtcompatible-nxp-lpc-i2c"><code>nxp,lpc-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">改进型集成电路间总线（I3C）</td>
<td>片上（On-Chip）</td>
<td>NXP MCUX I3C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L665">已禁用：1</a>）</td>
<td><a href="../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c"><code>nxp,mcux-i3c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt685_aud_evk/mimxrt685_aud_evk_mimxrt685s_cm33.dts?plain=1#L35">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP引脚中断及模式匹配引擎（PINT）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L293">已启用：1</a>）</td>
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
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt685_aud_evk/mimxrt685_aud_evk_mimxrt685s_cm33.dts?plain=1#L51">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>用作Zephyr邮箱（MBOX）的NXP i.MX消息单元（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L714">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P047_NXPiMX消息单元邮箱绑定.md#dtbinding-nxp-mbox-imx-mu"><code>nxp,mbox-imx-mu</code></a></td>
</tr>
<tr>
<td rowspan="1">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX RTxxx DSP控制驱动，适用于i.MX RT600 HiFi 4 DSP（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L57">已禁用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P004_nxp_rt600-dsp-ctrl.md#std-dtcompatible-nxp-rt600-dsp-ctrl"><code>nxp,rt600-dsp-ctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">内存管理单元／内存保护单元（MMU / MPU）</td>
<td>片上（On-Chip）</td>
<td>ARMv8-M存储器保护单元（MPU / Memory Protection Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L36">已启用：1</a>）</td>
<td><a href="../memory_protection_binding_reference/P007_arm_armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu"><code>arm,armv8m-mpu</code></a></td>
</tr>
<tr>
<td rowspan="2">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>NXP FlexSPI NOR闪存（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt685_aud_evk/mimxrt685_aud_evk_mimxrt685s_cm33.dts?plain=1#L87">已启用：1</a>）</td>
<td><a href="../mtd_microchip_nordic_nxp_binding_reference/P023_nxp_imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor"><code>nxp,imx-flexspi-nor</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt685_aud_evk/mimxrt685_aud_evk_mimxrt685s_cm33.dts?plain=1#L99">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">多路复用器（MUX）</td>
<td>片上（On-Chip）</td>
<td>NXP输入复用器（INPUTMUX）外设绑定（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L170">已禁用：1</a>）</td>
<td><a href="../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux"><code>nxp,inputmux</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>LPC I/O引脚配置（IOCON）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L154">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P007_nxp_lpc-iocon.md#std-dtcompatible-nxp-lpc-iocon"><code>nxp,lpc-iocon</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>RT600／RT500引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L158">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P018_nxp_rt-iocon-pinctrl.md#std-dtcompatible-nxp-rt-iocon-pinctrl"><code>nxp,rt-iocon-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>NXP状态可配置定时器（SCTimer）脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L529">已禁用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P012_nxp_sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm"><code>nxp,sctimer-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>NXP RSTCTL外设复位控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L225">已启用：2</a>）</td>
<td><a href="../reset_controller_binding_reference/P011_nxp_rstctl.md#std-dtcompatible-nxp-rstctl"><code>nxp,rstctl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Kinetis真随机数发生器（TRNG / True Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L522">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P020_nxp_kinetis-trng.md#std-dtcompatible-nxp-kinetis-trng"><code>nxp,kinetis-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>NXP LPC实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L510">已禁用：1</a>）</td>
<td><a href="../microchip_microcrystal_nxp_rtc_binding_reference/P013_nxp_lpc-rtc.md#std-dtcompatible-nxp-lpc-rtc"><code>nxp,lpc-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>NXP i.MX USDHC控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L557">已禁用：2</a>）</td>
<td><a href="../sdhc_binding_reference/P014_nxp_imx-usdhc.md#std-dtcompatible-nxp-imx-usdhc"><code>nxp,imx-usdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>LPC通用同步异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L305">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P014_nxp_lpc-usart.md#std-dtcompatible-nxp-lpc-usart"><code>nxp,lpc-usart</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>NXP FlexSPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L133">已启用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P001_nxp_imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi"><code>nxp,imx-flexspi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP LPC串行外设接口（SPI）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L407">已禁用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P003_nxp_lpc-spi.md#std-dtcompatible-nxp-lpc-spi"><code>nxp,lpc-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L96">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>i.MX RT5xx／6xx上的NXP操作系统定时器（OS Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L502">已启用：1</a>）</td>
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
<td>NXP LPCIP3511 USB设备模式（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L393">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P008_nxp_lpcip3511.md#std-dtcompatible-nxp-lpcip3511"><code>nxp,lpcip3511</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>NXP USB高速物理层（High Speed PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L401">已禁用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P013_nxp_usbphy.md#std-dtcompatible-nxp-usbphy"><code>nxp,usbphy</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>LPC窗口看门狗定时器（Windowed Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/imxrt/imxrt6xx/nxp_rt6xx_common.dtsi?plain=1#L539">已禁用：2</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P011_nxp_lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt"><code>nxp,lpc-wwdt</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

MIMXRT685 SoC提供IOCON寄存器，用于配置引脚功能。

<table>
<tr>
<th>名称（Name）</th>
<th>功能（Function）</th>
<th>用途（Usage）</th>
</tr>
<tr>
<td>PIO0_2</td>
<td>通用同步异步收发器（USART）</td>
<td>USART接收（RX）</td>
</tr>
<tr>
<td>PIO0_1</td>
<td>通用同步异步收发器（USART）</td>
<td>USART发送（TX）</td>
</tr>
<tr>
<td>PIO0_14</td>
<td>通用输入输出（GPIO）</td>
<td>绿色LED（GREEN LED）</td>
</tr>
<tr>
<td>PIO0_26</td>
<td>通用输入输出（GPIO）</td>
<td>蓝色LED（BLUE LED）</td>
</tr>
<tr>
<td>PIO0_31</td>
<td>通用输入输出（GPIO）</td>
<td>红色LED（RED LED）</td>
</tr>
<tr>
<td>PIO1_1</td>
<td>通用输入输出（GPIO）</td>
<td>SW1</td>
</tr>
<tr>
<td>PIO0_10</td>
<td>通用输入输出（GPIO）</td>
<td>SW2</td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

MIMXRT685-AUD-EVK配置为使用操作系统事件定时器（OS Event Timer）作为系统时钟源。

<a id="serial-port"></a>

### 串口（Serial Port）

MIMXRT685 SoC有8路FLEXCOMM串行通信接口，一路配置为控制台USART，其余未使用。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`mimxrt685_aud_evk`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

烧录及调试都使用调试探针，此板默认使用LPC-Link2。

<a id="tab-0-TGlua1NlcnZlciBDTVNJUy1EQVA="></a>

<a id="tab-0-Skxpbms="></a>

<a id="panel-0-TGlua1NlcnZlciBDTVNJUy1EQVA="></a>

**LinkServer CMSIS-DAP**


1. 安装LinkServer调试主机工具并加入搜索路径。LinkServer兼容板载调试器默认提供的CMSIS-DAP固件。（[LinkServer调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#linkserver-debug-host-tools)）

此板默认运行工具为LinkServer。

```text
west flash
west debug
```

<a id="panel-0-Skxpbms="></a>

**JLink**


1. 安装J-Link调试主机工具（Debug Host Tools），并确保工具位于搜索路径中。（[J-Link主机调试工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#jlink-debug-host-tools)）

```text
west flash -r jlink
west debug -r jlink
```

<a id="configuring-a-console"></a>

### 配置控制台（Configuring a Console）

用USB线缆将PC连接调试USB端口，在所选串口终端（如minicom、PuTTY）中使用以下设置：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

<a id="flashing"></a>

### 烧录（Flashing）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例，默认使用LinkServer调试主机工具。（[LinkServer调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#linkserver-debug-host-tools)）

```text
# From the root of the zephyr repository
west build -b mimxrt685_aud_evk/mimxrt685s/cm33 samples/hello_world
west flash
```

打开串口终端，复位开发板（按下RESET按键），应能在终端中看到以下消息：

```text
***** Booting Zephyr OS v4.x.x *****
Hello World! mimxrt685_aud_evk/mimxrt685s/cm33
```

<a id="debugging"></a>

### 调试（Debugging）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用为例，默认使用LinkServer调试主机工具。（[LinkServer调试主机工具（Debug Host Tools）](https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#linkserver-debug-host-tools)）

```text
# From the root of the zephyr repository
west build -b mimxrt685_aud_evk/mimxrt685s/cm33 samples/hello_world
west debug
```

打开串口终端，在调试器中单步运行应用，应能在终端中看到以下消息：

```text
***** Booting Zephyr OS v4.x.x *****
Hello World! mimxrt685_aud_evk/mimxrt685s/cm33
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

本页为音频专用MIMXRT685-AUD-EVK，使用CS42448编解码器，默认LinkServer；区别于普通RT685 EVK。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)：HTTP Error 403: Forbidden。
- [Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)：HTTP Error 403: Forbidden。
- [Training-Zephyr-Getting-Started.html](https://mcuxpresso.nxp.com/mcux-vscode/latest/html/Training-Zephyr-Getting-Started.html)：HTTP Error 404: Not Found。
- [zephyr](https://nxp.com/zephyr)：HTTP Error 404: Not Found。
- [RT600.pdf](https://www.nxp.com/docs/en/data-sheet/RT600.pdf)：HTTP Error 404: Not Found。
- [i-mx-rt600-crossover-mcu-with-arm-cortex-m33-and-dsp-cores:i.MX-RT600](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt600-crossover-mcu-with-arm-cortex-m33-and-dsp-cores:i.MX-RT600)：HTTP Error 404: Not Found。
- [Download?colCode=UM11147](https://www.nxp.com/webapp/Download?colCode=UM11147)：HTTP Error 404: Not Found。

---

[上一章](P005_MIMXRT595-EVK.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_MIMXRT685-EVK.md)
