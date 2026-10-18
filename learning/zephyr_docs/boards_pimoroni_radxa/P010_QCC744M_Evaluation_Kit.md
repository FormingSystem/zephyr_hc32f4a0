---
id: learning.zephyr-docs.boards-pimoroni-radxa.page-10
title: QCC744M Evaluation Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/qcom/qcc744m_evk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="qcc744m_evk"></a>

# 第10章\_QCC744M评估套件（Evaluation Kit）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qcom/qcc744m_evk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/qcc744m_evk.webp](images/qcc744m_evk.webp)](images/qcc744m_evk.webp)

QCC744M评估套件（Evaluation Kit）

名称（Name）：

`qcc744m_evk`

厂商（Vendor）：

[Qualcomm Technologies, Inc](https://docs.zephyrproject.org/latest/boards/index.html#vendor=qcom)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[`riscv`](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[bl618m05q2i](https://docs.zephyrproject.org/latest/boards/index.html#soc=bl618m05q2i)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/qcom/qcc744m_evk/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

QCC744M评估板搭载QCC744M模块，内含QCC744-2 SoC、4 MB伪静态RAM（PSRAM）及外接8 MB闪存芯片。Qualcomm QCC74x是一款三无线电（Tri-radio）芯片组，集成1×1 Wi-Fi 6、Bluetooth 5.4及IEEE 802.15.4，具备支持Thread及Zigbee的能力；处理器为最高320 MHz的32位RISC-V MCU。它基于Bouffalo Lab BL61x系列芯片组，与后者大体等同。

<a id="hardware"></a>

## 硬件（Hardware）

Qualcomm QCC74x MCU的更多信息见：


- [Qualcomm QCC74x MCU数据手册（Datasheet）](https://docs.qualcomm.com/bundle/publicresource/topics/80-WL743-1)
- [Qualcomm QCC74x MCU编程手册（Programming Manual）](https://docs.qualcomm.com/bundle/publicresource/topics/80-58740-1/)
- [Qualcomm QCC744M EVK快速入门指南（Quick Start Guide）](https://docs.qualcomm.com/bundle/publicresource/topics/80-WL740-250/landingpage.html)
- [Qualcomm QCC74x SDK](https://git.codelinaro.org/clo/qcc7xx/QCCSDK-QCC74x)
- [qcc744m_evk原理图（Schematics）](https://docs.qualcomm.com/bundle/publicresource/80-78831-41_REV_AC_QCC744M_Evaluation_Kit_Reference_Schematic.pdf)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`qcc744m_evk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="qcc744m_evk-hw-features"></a>

<a id="qcc744m_evk-qcc744m_evk/bl618m05q2i-hw-features-section"></a>

#### `qcc744m_evk/bl618m05q2i`目标（Target）

<a id="qcc744m_evk-qcc744m_evk/bl618m05q2i-hw-features-panel"></a>

<a id="qcc744m_evk-qcc744m_evk/bl618m05q2i-hw-features-memory"></a>

该开发板目标的片上存储容量：480 KiB RAM、8 MiB Flash。

<a id="qcc744m_evk-qcc744m_evk/bl618m05q2i-hw-features-table"></a>

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
<td>玄铁E907处理器内核（Xuantie E907 Core CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L120">已启用：1</a>）</td>
<td><a href="../cpu_vendor_multiarc_binding_reference/P055_xuantie_e907.md#std-dtcompatible-xuantie-e907"><code>xuantie,e907</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>博流智能（Bouffalolab）模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L212">已禁用：1</a>）</td>
<td><a href="../hardware/P886_BouffaloLab模数转换器绑定.md#dtbinding-bflb-adc"><code>bflb,adc</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>片上（On-Chip）</td>
<td>博流智能片上低功耗蓝牙（BLE）控制器的蓝牙主机控制器接口（Bluetooth HCI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L29">已禁用：1</a>）</td>
<td><a href="../bluetooth_vendor_hci_binding_reference/P002_bflb_bt-hci.md#std-dtcompatible-bflb-bt-hci"><code>bflb,bt-hci</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>博流智能BL61x控制器局域网控制器（CAN Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L367">已禁用：1</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P004_bflb_bl61x-can.md#std-dtcompatible-bflb-bl61x-can"><code>bflb,bl61x-can</code></a></td>
</tr>
<tr>
<td rowspan="7">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L39">已启用：3</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L46">已禁用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>博流智能F32K时钟（Clock）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L60">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P022_bflb_f32k.md#std-dtcompatible-bflb-f32k"><code>bflb,f32k</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>博流智能锁相环设置（PLL Settings）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L75">已启用：2</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P025_bflb_pll.md#std-dtcompatible-bflb-pll"><code>bflb,pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>博流智能根时钟（Root Clock）：根据实际存在的时钟表示FCLK和HCLK，两者应保持一致（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P001_bflb_root-clk.md#std-dtcompatible-bflb-root-clk"><code>bflb,root-clk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>总线时钟（BCLK）或外设时钟（Peripheral Clock）：时钟源 → 分频器 → 当前时钟（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L99">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P013_bflb_bclk.md#std-dtcompatible-bflb-bclk"><code>bflb,bclk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>博流智能闪存时钟（BFLB Flash Clock）：时钟源 → 分频器 → CLK。目前只提供BL61x存储区1（Bank 1，即启动闪存）的设置（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L106">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P023_bflb_flash-clk.md#std-dtcompatible-bflb-flash-clk"><code>bflb,flash-clk</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>博流智能BL61x时钟控制器（Clock Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L195">已启用：1</a>）</td>
<td><a href="../clock_adi_atmel_bflb_binding_reference/P016_bflb_bl61x-clock-controller.md#std-dtcompatible-bflb-bl61x-clock-controller"><code>bflb,bl61x-clock-controller</code></a></td>
</tr>
<tr>
<td rowspan="3">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>博流智能通用定时器模块（General Purpose Timer Block）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L340">已禁用：1</a>）</td>
<td><a href="../counter_binding_reference/P014_bflb_timer.md#std-dtcompatible-bflb-timer"><code>bflb,timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>博流智能定时器通道（Timer Channel），用作计数器（Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L348">已禁用：2</a>）</td>
<td><a href="../counter_binding_reference/P013_bflb_timer-channel.md#std-dtcompatible-bflb-timer-channel"><code>bflb,timer-channel</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>博流智能实时时钟计数器（RTC Counter），基于HBN（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L447">已禁用：1</a>）</td>
<td><a href="../counter_binding_reference/P012_bflb_rtc.md#std-dtcompatible-bflb-rtc"><code>bflb,rtc</code></a></td>
</tr>
<tr>
<td rowspan="3">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>博流智能安全引擎（SEC Engine）的真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L224">已禁用：1</a>）</td>
<td><a href="../crypto_aes_sha_ccm_binding_reference/P006_bflb_sec-eng-trng.md#std-dtcompatible-bflb-sec-eng-trng"><code>bflb,sec-eng-trng</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>博流智能安全引擎（SEC Engine）的SHA硬件加速器（Hardware Accelerator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L232">已禁用：1</a>）</td>
<td><a href="../crypto_aes_sha_ccm_binding_reference/P005_bflb_sec-eng-sha.md#std-dtcompatible-bflb-sec-eng-sha"><code>bflb,sec-eng-sha</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>博流智能安全引擎（SEC Engine）的AES硬件加速器（Hardware Accelerator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L241">已禁用：1</a>）</td>
<td><a href="../crypto_aes_sha_ccm_binding_reference/P004_bflb_sec-eng-aes.md#std-dtcompatible-bflb-sec-eng-aes"><code>bflb,sec-eng-aes</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>博流智能直接存储器访问（DMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L408">已启用：1</a>）</td>
<td><a href="../dma_binding_reference/P012_bflb_dma.md#std-dtcompatible-bflb-dma"><code>bflb,dma</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>博流智能BL61x/BL808通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L168">已启用：1</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P006_bflb_bl61x_808-gpio.md#std-dtcompatible-bflb-bl61x_808-gpio"><code>bflb,bl61x_808-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>博流智能I2C接口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L266">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L299">已禁用：1</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P012_bflb_i2c.md#std-dtcompatible-bflb-i2c"><code>bflb,i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">低速率无线个域网（IEEE 802.15.4）</td>
<td>片上（On-Chip）</td>
<td>博流智能IEEE 802.15.4节点（Node）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L517">已禁用：1</a>）</td>
<td><a href="../lora_ieee802154_binding_reference/P002_bflb_ieee802154.md#std-dtcompatible-bflb-ieee802154"><code>bflb,ieee802154</code></a></td>
</tr>
<tr>
<td rowspan="2">输入（Input）</td>
<td>片上（On-Chip）</td>
<td>博流智能红外接收外设（Infrared Receiver Peripheral）。将VS1838B等二极管／接收器的输出连接到指定GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L277">已禁用：1</a>）</td>
<td><a href="../input_adc_touch_matrix_binding_reference/P006_bflb_irx.md#std-dtcompatible-bflb-irx"><code>bflb,irx</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qcom/qcc744m_evk/qcc744m_evk.dts?plain=1#L19">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>芯来增强型内核本地中断控制器（Nuclei ECLIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L135">已启用：1</a>）</td>
<td><a href="../riscv_interrupt_binding_reference/P005_nuclei_eclic.md#std-dtcompatible-nuclei-eclic"><code>nuclei,eclic</code></a></td>
</tr>
<tr>
<td rowspan="3">存储器控制器（Memory Controller）</td>
<td>片上（On-Chip）</td>
<td>串行闪存控制器（Serial Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L376">已启用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P008_bflb_sf-controller.md#std-dtcompatible-bflb-sf-controller"><code>bflb,sf-controller</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>串行闪存控制器存储区（Serial Flash Controller Bank）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L386">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L394">已禁用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P007_bflb_sf-bank.md#std-dtcompatible-bflb-sf-bank"><code>bflb,sf-bank</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>BL61x伪静态随机存储器控制器（PSRAM / Pseudo-Static RAM Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L462">已启用：1</a>）</td>
<td><a href="../memory_controller_hyperbus_smc_binding_reference/P004_bflb_bl61x-psram.md#std-dtcompatible-bflb-bl61x-psram"><code>bflb,bl61x-psram</code></a></td>
</tr>
<tr>
<td rowspan="1">MIPI 显示总线接口（MIPI-DBI）</td>
<td>片上（On-Chip）</td>
<td>博流智能MIPI显示总线接口控制器（BFLB MIPI DBI Controller）。用于不完全符合MIPI DBI的器件时，例如SSD1327这类整个命令阶段都要保持DC置位、而非先DC再数据的器件，必须使用<code>cs-gpios</code>和<code>dc-gpio</code>，通过软件在命令期间保持这些线路状态，不能使用硬件DC和CS（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L288">已禁用：1</a>）</td>
<td><a href="../mipi_dbi_dsi_binding_reference/P001_bflb_dbi.md#std-dtcompatible-bflb-dbi"><code>bflb,dbi</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>板载（On-Board）</td>
<td>博流智能串行闪存控制器中的闪存（Serial Flash Controller Flash）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qcom/qcc744m_evk/qcc744m.dtsi?plain=1#L41">已启用：1</a>）</td>
<td><a href="../mtd_atmel_bouffalo_binding_reference/P012_bflb_sf-flash.md#std-dtcompatible-bflb-sf-flash"><code>bflb,sf-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">一次性可编程存储器（OTP Memory）</td>
<td>片上（On-Chip）</td>
<td>博流智能电子熔丝（Efuse）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L469">已启用：1</a>）</td>
<td><a href="../otp_binding_reference/P002_bflb_efuse.md#std-dtcompatible-bflb-efuse"><code>bflb,efuse</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>博流智能引脚控制节点（Pinctrl Node）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L159">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P016_bflb_pinctrl.md#std-dtcompatible-bflb-pinctrl"><code>bflb,pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理（Power Management）</td>
<td>片上（On-Chip）</td>
<td>博流智能电源控制器（Power Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L418">已启用：1</a>）</td>
<td><a href="../power_control_binding_reference/P002_bflb_power-controller.md#std-dtcompatible-bflb-power-controller"><code>bflb,power-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>博流智能脉宽调制2（PWM 2）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L321">已禁用：1</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P011_bflb_pwm-2.md#std-dtcompatible-bflb-pwm-2"><code>bflb,pwm-2</code></a></td>
</tr>
<tr>
<td rowspan="3">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>博流智能HBN SoC电压稳压器（Voltage Regulator），供CPU、存储器等使用。它是标称电压1.10 V的低压差稳压器（LDO）。具有两种模式，但仅在进入睡眠模式时切换，且两种模式不共用设置区域（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L429">已启用：1</a>）</td>
<td><a href="../hardware/P648_Bouffalo_SoC稳压器绑定.md#dtbinding-bflb-soc-regulator"><code>bflb,soc-regulator</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>博流智能HBN RT电压稳压器，供实时时钟（RTC）使用。它是标称电压1.10 V的低压差稳压器（LDO）。具有两种模式，但仅在进入睡眠模式时切换，且两种模式不共用设置区域（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L435">已启用：1</a>）</td>
<td><a href="../hardware/P647_Bouffalo_RT稳压器绑定.md#dtbinding-bflb-rt-regulator"><code>bflb,rt-regulator</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>博流智能HBN AON电压稳压器，供始终开启区域（Always ON Section）使用。它是标称电压1.10 V的低压差稳压器（LDO）。具有两种模式，但仅在进入睡眠模式时切换，且两种模式不共用设置区域（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L441">已启用：1</a>）</td>
<td><a href="../hardware/P646_Bouffalo_AON稳压器绑定.md#dtbinding-bflb-aon-regulator"><code>bflb,aon-regulator</code></a></td>
</tr>
<tr>
<td rowspan="1">SD 主机控制器（SDHC）</td>
<td>片上（On-Chip）</td>
<td>博流智能安全数字主机控制器（SD Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L476">已禁用：1</a>）</td>
<td><a href="../sdhc_binding_reference/P004_bflb_sdhc.md#std-dtcompatible-bflb-sdhc"><code>bflb,sdhc</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>博流智能片内温度传感器（TSEN / Internal Die Temperature Sensor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L23">已禁用：1</a>）</td>
<td><a href="../sensor_ams_aosong_bosch_binding_reference/P023_bflb_tsen.md#std-dtcompatible-bflb-tsen"><code>bflb,tsen</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>博流智能通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L250">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L258">已禁用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P013_bflb_uart.md#std-dtcompatible-bflb-uart"><code>bflb,uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>博流智能串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L310">已启用：1</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P010_bflb_spi.md#std-dtcompatible-bflb-spi"><code>bflb,spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L531">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L539">已禁用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>RISC-V机器模式定时器（Machine Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L151">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P011_riscv_machine-timer.md#std-dtcompatible-riscv-machine-timer"><code>riscv,machine-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>博流智能看门狗定时器（Watchdog Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L331">已禁用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P010_bflb_wdt.md#std-dtcompatible-bflb-wdt"><code>bflb,wdt</code></a></td>
</tr>
<tr>
<td rowspan="1">无线局域网（Wi-Fi）</td>
<td>片上（On-Chip）</td>
<td>博流智能“WiFi6”无线局域网媒体访问控制器（WiFi MAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L485">已禁用：1</a>）</td>
<td><a href="../wifi_esp_hosted_airoc_binding_reference/P003_bflb_wifi6.md#std-dtcompatible-bflb-wifi6"><code>bflb,wifi6</code></a></td>
</tr>
</table>

<a id="serial-port"></a>

### 串口（Serial Port）

qcc744m_evk默认使用UART0串口，连接板载USB转串口转换器，同时用于编程及控制台。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

<a id="samples"></a>

### 示例（Samples）


1. 构建Zephyr内核和[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例应用：

  ```text
  # From the root of the zephyr repository
  west build -b qcc744m_evk samples/hello_world
  ```
2. 目前west flash无法烧录QCC74x MCU。可先从[Qualcomm QCC74x SDK](https://git.codelinaro.org/clo/qcc7xx/QCCSDK-QCC74x)获取QConn Flash，再按以下步骤操作：


  - 打开QConn Flash。
  - 进入Flash Utils选项卡。
  - 选择合适的烧录端口及接口。
  - 按住左侧BOOT键，同时按右侧RESET键复位开发板，进入烧录模式（Flash Mode）。
  - 在Flash Program中，选择SDK内的bsp/board/qcc744dk/config/boot2_qcc743_isp_release_v8.1.9.bin，将地址设为0x0。
  - 按Download下载按钮。
  - 再次进入烧录模式。
  - 在Flash Program中，选择构建目录内的zephyr.bin，将地址设为0x2000。
  - 再次按Download下载按钮。

  至此已完成烧录。第一个二进制文件写入0x0后，只要其所在闪存区域没有被擦除，就无需重新写入该文件。
3. 使用常用终端程序接收输出。Linux下的终端设备应为/dev/ttyACM1，例如：

  ```text
  $ screen /dev/ttyACM1 115200
  ```

  连接参数应配置如下：


  - 速率（Speed）：115200波特率
  - 数据位（Data）：8位
  - 奇偶校验（Parity）：无（None）
  - 停止位（Stop Bits）：1位

  随后按下并松开RESET键。

  ```text
  *** Booting Zephyr OS build v4.3.0 ***
  Hello World! qcc744m_evk/bl618m05q2i
  ```

至此，qcc744m_evk已配置完成并运行Zephyr。

## 译注

QCC744M尚不支持west flash；QConn Flash先将SDK引导二进制写入0x0，再将zephyr.bin写入0x2000。首次写入的引导二进制在其区域未擦除时无需重复写入。

---

[上一章](P009_Qualcomm_Technologies_Inc..md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_Decawave_DWM1001.md)
