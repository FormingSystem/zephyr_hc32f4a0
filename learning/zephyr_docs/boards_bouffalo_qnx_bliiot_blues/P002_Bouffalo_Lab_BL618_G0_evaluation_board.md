---
id: learning.zephyr-docs.boards-bouffalo-qnx-bliiot-blues.page-2
title: Bouffalo Lab BL618 G0 evaluation board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/bflb/bl61x/bl618g0/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="bl618g0"></a>

# 第2章\_博流BL618 G0评估板（Evaluation Board）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/bflb/bl61x/bl618g0/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../../_images/bl618g0.webp](images/bl618g0.webp)](images/bl618g0.webp)

博流BL618 G0评估板（Evaluation Board）

名称（Name）：

`bl618g0`

厂商（Vendor）：

[博流（南京）有限公司（Bouffalo Lab）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=bflb)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[bl618m05q2i](https://docs.zephyrproject.org/latest/boards/index.html#soc=bl618m05q2i)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/bflb/bl61x/bl618g0/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

博流BL618 G0是基于BL618 SoC的评估板。BL618是一款支持Wi-Fi 6、BLE 5.3及IEEE 802.15.4（Zigbee／Thread）的RISC-V微控制器，最高时钟320 MHz，具有480 KB SRAM。

开发板具有以下特性：


- BL618M05Q2I SoC，采用BL618内核
- W25Q64 8 MB外部SPI闪存
- 32 MB嵌入式伪静态随机存储器（PSRAM）
- 板载CK-Link调试器，无需外部探针
- 通过USB-C提供USB 2.0高速OTG
- MicroSD（TF）卡槽
- IPEX天线连接器
- 扩展排针引出全部未使用的GPIO
- 支持可选扩展模块：I2S音频、SPI显示屏及数字视频端口摄像头（DVP Camera）
- 一个用户LED，GPIO32
- 一个用户按键，GPIO33
- 复位（Reset）与启动（Boot）按键

<a id="hardware"></a>

## 硬件（Hardware）

博流智能（Bouffalo Lab）BL-61x微控制器的更多信息：


- [博流智能BL61x微控制器数据手册（MCU Datasheet）](https://github.com/bouffalolab/bl_docs/tree/main/BL616_DS/en)
- [博流智能开发专区（Bouffalo Lab Development Zone）](https://dev.bouffalolab.com/home?id=guest)
- [博流BL618 G0开发板（Board）](https://verimake.com/d/260-bl618)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`bl618g0`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="bl618g0-hw-features"></a>

<a id="bl618g0-bl618g0/bl618m05q2i-hw-features-section"></a>

#### `bl618g0/bl618m05q2i`目标（Target）

<a id="bl618g0-bl618g0/bl618m05q2i-hw-features-panel"></a>

<a id="bl618g0-bl618g0/bl618m05q2i-hw-features-memory"></a>

该开发板目标的片上存储容量：320 KiB RAM、8 MiB Flash。

<a id="bl618g0-bl618g0/bl618m05q2i-hw-features-table"></a>

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
<td>博流智能片上低功耗蓝牙（BLE）控制器的蓝牙主机控制器接口（Bluetooth HCI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L29">已启用：1</a>）</td>
<td><a href="../bluetooth_vendor_hci_binding_reference/P002_bflb_bt-hci.md#std-dtcompatible-bflb-bt-hci"><code>bflb,bt-hci</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>博流智能BL61x控制器局域网控制器（CAN Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L367">已启用：1</a>）</td>
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
<td>博流智能安全引擎（SEC Engine）的真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L224">已启用：1</a>）</td>
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
<td>博流智能I2C接口（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L266">已禁用：2</a>）</td>
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
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/bflb/bl61x/bl618g0/bl618g0.dts?plain=1#L45">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>芯来增强型内核本地中断控制器（Nuclei ECLIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L135">已启用：1</a>）</td>
<td><a href="../riscv_interrupt_binding_reference/P005_nuclei_eclic.md#std-dtcompatible-nuclei-eclic"><code>nuclei,eclic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/bflb/bl61x/bl618g0/bl618g0.dts?plain=1#L36">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
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
<td>博流智能串行闪存控制器中的闪存（Serial Flash Controller Flash）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/bflb/bl61x/bl618g0/bl618g0.dts?plain=1#L76">已启用：1</a>）</td>
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
<td>博流智能安全数字主机控制器（SD Host Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L476">已启用：1</a>）</td>
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
<td>博流智能串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L310">已禁用：1</a>）</td>
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
<td>博流智能“WiFi6”无线局域网媒体访问控制器（WiFi MAC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/bflb/bl61x.dtsi?plain=1#L485">已启用：1</a>）</td>
<td><a href="../wifi_esp_hosted_airoc_binding_reference/P003_bflb_wifi6.md#std-dtcompatible-bflb-wifi6"><code>bflb,wifi6</code></a></td>
</tr>
</table>

<a id="system-clock"></a>

### 系统时钟（System Clock）

BL618 G0评估板配置为以最高320 MHz运行。

<a id="serial-port"></a>

### 串口（Serial Port）

`bl618g0`默认使用UART0，连接板载CK-Link的USB转UART接口，同时用于烧录及控制台输出。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`bl618g0`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>bflb_mcu_tool</td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

<a id="samples"></a>

### 示例（Samples）


1. 构建Zephyr内核和[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)示例应用：

  ```text
  # From the root of the zephyr repository
  west build -b bl618g0 samples/hello_world
  west flash
  ```
2. 运行常用终端程序查看输出：

  ```text
  $ screen /dev/ttyACM0 115200
  ```

  连接参数应配置如下：

  > - 速率（Speed）：115200波特率
  > - 数据位（Data）：8位
  > - 奇偶校验（Parity）：无（None）
  > - 停止位（Stop Bits）：1位

  然后按下并松开RST复位按键。

  ```text
  *** Booting Zephyr OS build v4.4.0 ***
  Hello World! bl618g0/bl618m05q2i
  ```

至此，`bl618g0`已配置完成并运行Zephyr。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [260-bl618](https://verimake.com/d/260-bl618)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1010)>。

---

[上一章](P001_BL604E_IOT_DVK_development_board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_Bouffalo_Lab_BL706-IoT-DVK.md)
