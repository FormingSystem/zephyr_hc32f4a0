---
id: learning.zephyr-docs.boards-arduino.page-10
title: Arduino Nesso N1
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/arduino/nesso_n1/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="arduino_nesso_n1"></a>

# 第10章\_Arduino Nesso N1

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/arduino/nesso_n1/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/arduino_nesso_n1.webp](images/arduino_nesso_n1.webp)](images/arduino_nesso_n1.webp)

Arduino Nesso N1

名称（Name）：

`arduino_nesso_n1`

厂商（Vendor）：

[Arduino](https://docs.zephyrproject.org/latest/boards/index.html#vendor=arduino)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[esp32c6](https://docs.zephyrproject.org/latest/boards/index.html#soc=esp32c6)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/arduino/nesso_n1/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id13"></a>

[Arduino Nesso N1](https://docs.arduino.cc/hardware/nesso-n1/)是一款紧凑型多协议物联网（IoT）开发板，由Arduino与M5Stack共同设计，基于Espressif ESP32-C6 32位RISC-V片上系统（SoC），最高运行频率160 MHz。它在同一设备中集成Wi-Fi 6、Bluetooth LE 5.3、IEEE 802.15.4（Thread/Zigbee）及Sub-GHz LoRa连接。更多信息见Arduino Nesso N1[注6](#id12)。

<a id="hardware"></a>

## 硬件（Hardware）

开发板的系统I2C总线上连接Bosch BMI270六轴惯性测量单元（IMU），SPI上连接Semtech SX1262 LoRa收发器；另配有1.14英寸彩色薄膜晶体管显示屏（TFT）、电容触摸、红外发射器（IR Transmitter）、可编程按键及250 mAh锂聚合物电池（LiPo），电池由板载电量计（Fuel Gauge）管理。USB-C接到ESP32-C6原生USB-Serial-JTAG接口，烧录和串口控制台共用一根线，无需外部编程器。

<a id="esp32-c6-features"></a>

### ESP32-C6特性（Features）

ESP32-C6是乐鑫（Espressif）首款集成2.4 GHz Wi-Fi 6、蓝牙5.3低功耗（Bluetooth LE）和IEEE 802.15.4协议的Wi-Fi 6片上系统（SoC）。原文介绍其具有业界领先的射频（RF）性能、可靠的安全功能和多种存储资源，面向物联网（IoT）产品。它包含一个最高160 MHz的高性能32位RISC-V处理器（HP Processor），以及一个最高20 MHz的低功耗32位RISC-V处理器（LP Processor），具有320 KB ROM、512 KB SRAM，并使用外部闪存（Flash）。

ESP32-C6包含以下特性：


- 32位RISC-V内核微控制器（Microcontroller），最高时钟频率160 MHz
- 400 KB内部随机存储器（RAM）
- 2.4 GHz Wi-Fi 802.11ax
- 完全兼容IEEE 802.11b/g/n协议
- 低功耗蓝牙（Bluetooth LE），通过Bluetooth 5.3认证
- 内部Wi-Fi与蓝牙共存机制（Co-existence Mechanism），共享同一天线
- IEEE 802.15.4，支持Zigbee和Thread

数字接口（Digital Interfaces）：


- 30个GPIO引脚（QFN40封装）或22个GPIO引脚（QFN32封装）
- 2 个 UART 接口。
- 1路低功耗通用异步收发器（LP UART）
- 1路通用串行外设接口（General-purpose SPI）
- 1 个 I2C 接口。
- 1路低功耗I2C接口（LP I2C）
- 1 个 I2S 接口。
- 1个脉冲计数器（Pulse Counter）
- 1个USB串口／JTAG控制器（USB Serial/JTAG Controller）
- 1个TWAI®控制器，兼容ISO 11898-1，即CAN 2.0规范（CAN Specification 2.0）
- 1个SDIO 2.0从控制器（Slave Controller）
- LED脉宽调制控制器（PWM Controller），最多6个通道
- 1个电机控制脉宽调制器（MCPWM）
- 1个遥控外设（Remote Control Peripheral）
- 1个并行输入输出接口（PARLIO / Parallel IO Interface）
- 通用直接存储器访问控制器（GDMA / General DMA Controller），具有3个发送通道和3个接收通道
- 事件任务矩阵（ETM / Event Task Matrix）

模拟接口（Analog Interfaces）：


- 1个12位逐次逼近模数转换器（SAR ADC），最多7个通道
- 1个温度传感器（Temperature Sensor）

定时器（Timers）：


- 1个52位系统定时器（System Timer）
- 1个54位通用定时器（General-purpose Timer）
- 3个看门狗定时器（Watchdog Timers）
- 1个模拟看门狗定时器（Analog Watchdog Timer）

低功耗（Low Power）：


- 针对典型场景设计的4种电源模式：活动（Active）、调制解调器睡眠（Modem-sleep）、浅睡眠（Light-sleep）和深度睡眠（Deep-sleep）

Security:


- 安全启动（Secure Boot）
- 闪存加密（Flash Encryption）
- 4 Kbit一次性可编程存储器（OTP），用户最多可使用1792位
- 密码硬件加速（Cryptographic Hardware Acceleration）：AES-128/256、椭圆曲线密码（ECC）、HMAC、RSA、SHA、数字签名（Digital Signature）和散列（Hash）
- 随机数发生器（RNG / Random Number Generator）

<a id="low-power-cpu-lp-core"></a>

### 低功耗处理器（LP CORE / Low-Power CPU）

ESP32-C6片上系统（SoC）具有两个RISC-V内核：高性能内核（HP CORE / High-Performance Core）和低功耗内核（LP CORE / Low-Power Core）。LP内核功耗极低，并带有中断控制器（Interrupt Controller）、调试模块（Debug Module）和用于访问存储器及外设的系统总线接口（System Bus Interface）。

LP内核默认处于睡眠模式（Sleep Mode），有以下两类应用场景：


- 对功耗不敏感的场景（Power-insensitive Scenario）：高性能处理器（HP Core）活动时，LP内核可以协助完成一些对速度和效率要求不高的控制与计算任务。
- 对功耗敏感的场景（Power-sensitive Scenario）：HP处理器为了省电而处于掉电状态（Power-down State）时，可以唤醒LP内核来处理外部唤醒事件（Wake-up Events）。

LP内核支持已完整集成到[系统构建（Sysbuild / System Build）](../sysbuild/P001_系统构建.md#sysbuild)中。可以在项目中加入以下配置来启用LP内核：

```text
CONFIG_ESP32_ULP_COPROC_ENABLED=y
```

代码参考见[低功耗处理器（LP CORE / Low-Power CPU）](../board_samples/P101_低功耗CPU示例目录.md#low-power-cpu-lp-core)目录。

<a id="id3"></a>

<a id="id5"></a>

更多信息见[ESP32-C6数据手册（Datasheet）](https://www.espressif.com/sites/default/files/documentation/esp32-c6_datasheet_en.pdf)[注1](#id2)或[ESP32-C6技术参考手册（Technical Reference Manual）](https://espressif.com/sites/default/files/documentation/esp32-c6_technical_reference_manual_en.pdf)[注2](#id4)。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`arduino_nesso_n1`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="arduino_nesso_n1-hw-features"></a>

<a id="arduino_nesso_n1-arduino_nesso_n1/esp32c6/hpcore-hw-features-section"></a>

#### `arduino_nesso_n1/esp32c6/hpcore`目标（Target）

<a id="arduino_nesso_n1-arduino_nesso_n1/esp32c6/hpcore-hw-features-panel"></a>

<a id="arduino_nesso_n1-arduino_nesso_n1/esp32c6/hpcore-hw-features-memory"></a>

该开发板目标的片上存储容量：512 KiB RAM、16 MiB Flash。

<a id="arduino_nesso_n1-arduino_nesso_n1/esp32c6/hpcore-hw-features-table"></a>

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
<td>乐鑫（Espressif）RISC-V处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L36">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P024_espressif_riscv.md#std-dtcompatible-espressif-riscv"><code>espressif,riscv</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>ESP32模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L318">已禁用：1</a>）</td>
<td><a href="../hardware/P889_ESP32模数转换器绑定.md#dtbinding-espressif-esp32-adc"><code>espressif,esp32-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>片上（On-Chip）</td>
<td>乐鑫（Espressif）ESP32蓝牙主机控制器接口（Bluetooth HCI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L72">已启用：1</a>）</td>
<td><a href="../bluetooth_vendor_hci_binding_reference/P004_espressif_esp32-bt-hci.md#std-dtcompatible-espressif-esp32-bt-hci"><code>espressif,esp32-bt-hci</code></a></td>
</tr>
<tr>
<td rowspan="1">蜂鸣器（Buzzer）</td>
<td>板载（On-Board）</td>
<td>由GPIO驱动的有源蜂鸣器（Active Buzzer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/nesso_n1/arduino_nesso_n1_esp32c6_hpcore.dts?plain=1#L52">已启用：1</a>）</td>
<td><a href="../sound_haptic_binding_reference/P002_gpio-buzzer.md#std-dtcompatible-gpio-buzzer"><code>gpio-buzzer</code></a></td>
</tr>
<tr>
<td rowspan="1">控制器局域网（CAN）</td>
<td>片上（On-Chip）</td>
<td>ESP32双线汽车接口（TWAI / Two-Wire Automotive Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L247">已禁用：2</a>）</td>
<td><a href="../can_adi_atmel_nxp_binding_reference/P005_espressif_esp32-twai.md#std-dtcompatible-espressif-esp32-twai"><code>espressif,esp32-twai</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>ESP32时钟模块（Clock Module，电源与时钟控制器模块 / Power &amp; Clock Controller Module）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../clock_esp_infineon_microchip_binding_reference/P004_espressif_esp32-clock.md#std-dtcompatible-espressif-esp32-clock"><code>espressif,esp32-clock</code></a></td>
</tr>
<tr>
<td rowspan="3">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>ESP32通用定时器（General-purpose Timers）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L199">已禁用：2</a>）</td>
<td><a href="../counter_binding_reference/P017_espressif_esp32-timer.md#std-dtcompatible-espressif-esp32-timer"><code>espressif,esp32-timer</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ESP32计数器（Counters）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L209">已禁用：2</a>）</td>
<td><a href="../counter_binding_reference/P015_espressif_esp32-counter.md#std-dtcompatible-espressif-esp32-counter"><code>espressif,esp32-counter</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>基于RTC主定时器（Main Timer）的ESP32计数器驱动（Counter Driver）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L231">已禁用：1</a>）</td>
<td><a href="../counter_binding_reference/P016_espressif_esp32-rtc-timer.md#std-dtcompatible-espressif-esp32-rtc-timer"><code>espressif,esp32-rtc-timer</code></a></td>
</tr>
<tr>
<td rowspan="2">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>乐鑫（Espressif）ESP32 SHA硬件加速器（Hardware Accelerator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L449">已启用：1</a>）</td>
<td><a href="../crypto_aes_sha_ccm_binding_reference/P008_espressif_esp32-sha.md#std-dtcompatible-espressif-esp32-sha"><code>espressif,esp32-sha</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>乐鑫（Espressif）ESP32系列AES硬件加速器（Hardware Accelerator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L456">已启用：1</a>）</td>
<td><a href="../crypto_aes_sha_ccm_binding_reference/P007_espressif_esp32-aes.md#std-dtcompatible-espressif-esp32-aes"><code>espressif,esp32-aes</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>板载（On-Board）</td>
<td>Sitronix ST7789V显示控制器（Display Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/nesso_n1/arduino_nesso_n1_esp32c6_hpcore.dts?plain=1#L89">已启用：1</a>）</td>
<td><a href="../display_sinowealth_sitronix_solomon_binding_reference/P011_sitronix_st7789v.md#std-dtcompatible-sitronix-st7789v"><code>sitronix,st7789v</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>ESP32通用直接存储器访问（GDMA / General Direct Memory Access）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L328">已禁用：1</a>）</td>
<td><a href="../dma_binding_reference/P015_espressif_esp32-gdma.md#std-dtcompatible-espressif-esp32-gdma"><code>espressif,esp32-gdma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>ESP32闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L293">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P012_espressif_esp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller"><code>espressif,esp32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>ESP32通用输入输出控制器（GPIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L345">已启用：1</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P022_espressif_esp32-gpio.md#std-dtcompatible-espressif-esp32-gpio"><code>espressif,esp32-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Diodes/Pericom PI4IOE5V6408八位I2C总线I/O扩展器（Expander）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/nesso_n1/arduino_nesso_n1_esp32c6_hpcore.dts?plain=1#L159">已启用：2</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P016_diodes_pi4ioe5v6408.md#std-dtcompatible-diodes-pi4ioe5v6408"><code>diodes,pi4ioe5v6408</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>ESP32 I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L355">已启用：1</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P018_espressif_esp32-i2c.md#std-dtcompatible-espressif-esp32-i2c"><code>espressif,esp32-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间音频总线（I2S）</td>
<td>片上（On-Chip）</td>
<td>ESP32芯片间音频接口（I2S）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L366">已禁用：1</a>）</td>
<td><a href="../i2s_binding_reference/P003_espressif_esp32-i2s.md#std-dtcompatible-espressif-esp32-i2s"><code>espressif,esp32-i2s</code></a></td>
</tr>
<tr>
<td rowspan="1">低速率无线个域网（IEEE 802.15.4）</td>
<td>片上（On-Chip）</td>
<td>乐鑫（Espressif）ESP32 IEEE 802.15.4节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="../lora_ieee802154_binding_reference/P004_espressif_esp32-ieee802154.md#std-dtcompatible-espressif-esp32-ieee802154"><code>espressif,esp32-ieee802154</code></a></td>
</tr>
<tr>
<td rowspan="2">输入（Input）</td>
<td>板载（On-Board）</td>
<td>FT3267/FT5XX6/FT6XX6电容式触摸面板（Capacitive Touch Panels）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/nesso_n1/arduino_nesso_n1_esp32c6_hpcore.dts?plain=1#L150">已启用：1</a>）</td>
<td><a href="../input_adc_touch_matrix_binding_reference/P014_focaltech_ft5336.md#std-dtcompatible-focaltech-ft5336"><code>focaltech,ft5336</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/nesso_n1/arduino_nesso_n1_esp32c6_hpcore.dts?plain=1#L57">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ESP32中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L182">已启用：1</a>）</td>
<td><a href="../soc_interrupt_binding_reference/P005_espressif_esp32-intc.md#std-dtcompatible-espressif-esp32-intc"><code>espressif,esp32-intc</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/nesso_n1/arduino_nesso_n1_esp32c6_hpcore.dts?plain=1#L43">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">远距离无线通信（LoRa）</td>
<td>板载（On-Board）</td>
<td>Semtech SX1262 LoRa调制解调器（Modem）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/nesso_n1/arduino_nesso_n1_esp32c6_hpcore.dts?plain=1#L185">已启用：1</a>）</td>
<td><a href="../lora_ieee802154_binding_reference/P021_semtech_sx1262.md#std-dtcompatible-semtech-sx1262"><code>semtech,sx1262</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>ESP32软件邮箱（Soft Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L169">已启用：1</a>）</td>
<td><a href="../intercore_reference/P037_ESP32邮箱绑定.md#dtbinding-espressif-mbox-esp32"><code>espressif,mbox-esp32</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L301">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>ESP32引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L67">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P022_espressif_esp32-pinctrl.md#std-dtcompatible-espressif-esp32-pinctrl"><code>espressif,esp32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉冲输入输出（Pulse IO）</td>
<td>片上（On-Chip）</td>
<td>乐鑫遥控收发器（RMT / Remote Control Transceiver）pulse_io控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L463">已禁用：1</a>）</td>
<td><a href="../platform_rmt_openthread_binding_reference/P008_espressif_esp32-rmt.md#std-dtcompatible-espressif-esp32-rmt"><code>espressif,esp32-rmt</code></a></td>
</tr>
<tr>
<td rowspan="2">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>ESP32 LED控制（LEDC / LED Control）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L421">已禁用：1</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P015_espressif_esp32-ledc.md#std-dtcompatible-espressif-esp32-ledc"><code>espressif,esp32-ledc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ESP32电机控制脉宽调制器（MCPWM / Motor Control Pulse Width Modulator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L430">已禁用：1</a>）</td>
<td><a href="../pwm_adi_esp_infineon_binding_reference/P016_espressif_esp32-mcpwm.md#std-dtcompatible-espressif-esp32-mcpwm"><code>espressif,esp32-mcpwm</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>板载（On-Board）</td>
<td>固定电压稳压器（Fixed Voltage Regulators）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/nesso_n1/arduino_nesso_n1_esp32c6_hpcore.dts?plain=1#L73">已启用：1</a>）</td>
<td><a href="../hardware/P635_固定稳压器设备树绑定.md#dtbinding-regulator-fixed"><code>regulator-fixed</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>ESP32真随机数发生器（TRNG / True Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L240">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P007_espressif_esp32-trng.md#std-dtcompatible-espressif-esp32-trng"><code>espressif,esp32-trng</code></a></td>
</tr>
<tr>
<td rowspan="3">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>ESP32内部温度传感器（Internal Temperature Sensor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L311">已禁用：1</a>）</td>
<td><a href="../sensor_espressif_honeywell_invensense_binding_reference/P001_espressif_esp32-temp.md#std-dtcompatible-espressif-esp32-temp"><code>espressif,esp32-temp</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>BMI270惯性测量单元（IMU / Inertial Measurement Unit）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/nesso_n1/arduino_nesso_n1_esp32c6_hpcore.dts?plain=1#L144">已启用：1</a>）</td>
<td><a href="../compatible_binding_reference/P016_bosch_bmi270.md#std-dtcompatible-bosch-bmi270"><code>bosch,bmi270</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ESP32脉冲计数器（PCNT / Pulse Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L440">已禁用：1</a>）</td>
<td><a href="../sensor_bosch_broadcom_espressif_binding_reference/P030_espressif_esp32-pcnt.md#std-dtcompatible-espressif-esp32-pcnt"><code>espressif,esp32-pcnt</code></a></td>
</tr>
<tr>
<td rowspan="3">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ESP32通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L380">已禁用：2</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P002_espressif_esp32-uart.md#std-dtcompatible-espressif-esp32-uart"><code>espressif,esp32-uart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ESP32低功耗通用异步收发器（Low Power UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L399">已禁用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P001_espressif_esp32-lpuart.md#std-dtcompatible-espressif-esp32-lpuart"><code>espressif,esp32-lpuart</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>ESP32通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L412">已启用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P003_espressif_esp32-usb-serial.md#std-dtcompatible-espressif-esp32-usb-serial"><code>espressif,esp32-usb-serial</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>ESP32串行外设接口控制器（SPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L265">已启用：1</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P014_espressif_esp32-spi.md#std-dtcompatible-espressif-esp32-spi"><code>espressif,esp32-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ESP32系统定时器（System Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L191">已启用：1</a>）</td>
<td><a href="../mcu_timer_binding_reference/P004_espressif_esp32-systimer.md#std-dtcompatible-espressif-esp32-systimer"><code>espressif,esp32-systimer</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>ESP32看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L275">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L284">已禁用：1</a>）</td>
<td><a href="../watchdog_binding_reference/P013_espressif_esp32-watchdog.md#std-dtcompatible-espressif-esp32-watchdog"><code>espressif,esp32-watchdog</code></a></td>
</tr>
<tr>
<td rowspan="1">无线局域网（Wi-Fi）</td>
<td>片上（On-Chip）</td>
<td>ESP32片上系统（SoC）Wi-Fi（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_common.dtsi?plain=1#L86">已启用：1</a>）</td>
<td><a href="../wifi_esp_hosted_airoc_binding_reference/P009_espressif_esp32-wifi.md#std-dtcompatible-espressif-esp32-wifi"><code>espressif,esp32-wifi</code></a></td>
</tr>
</table>

<a id="arduino_nesso_n1-arduino_nesso_n1/esp32c6/lpcore-hw-features-section"></a>

#### `arduino_nesso_n1/esp32c6/lpcore`目标（Target）

<a id="arduino_nesso_n1-arduino_nesso_n1/esp32c6/lpcore-hw-features-panel"></a>

<a id="arduino_nesso_n1-arduino_nesso_n1/esp32c6/lpcore-hw-features-memory"></a>

该开发板目标的片上存储容量：15 KiB RAM、16 MiB Flash。

<a id="arduino_nesso_n1-arduino_nesso_n1/esp32c6/lpcore-hw-features-table"></a>

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
<td>乐鑫（Espressif）RISC-V处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_lpcore.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P024_espressif_riscv.md#std-dtcompatible-espressif-riscv"><code>espressif,riscv</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>ESP32闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_lpcore.dtsi?plain=1#L86">已启用：1</a>）</td>
<td><a href="../flash_adi_microchip_nordic_binding_reference/P012_espressif_esp32-flash-controller.md#std-dtcompatible-espressif-esp32-flash-controller"><code>espressif,esp32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>用于LP内核的ESP32低功耗GPIO控制器（Low Power GPIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_lpcore.dtsi?plain=1#L113">已启用：1</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P023_espressif_esp32-lpgpio.md#std-dtcompatible-espressif-esp32-lpgpio"><code>espressif,esp32-lpgpio</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ESP32中断控制器（Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_lpcore.dtsi?plain=1#L77">已启用：1</a>）</td>
<td><a href="../soc_interrupt_binding_reference/P005_espressif_esp32-intc.md#std-dtcompatible-espressif-esp32-intc"><code>espressif,esp32-intc</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>ESP32软件邮箱（Soft Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_lpcore.dtsi?plain=1#L64">已启用：1</a>）</td>
<td><a href="../intercore_reference/P037_ESP32邮箱绑定.md#dtbinding-espressif-mbox-esp32"><code>espressif,mbox-esp32</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_lpcore.dtsi?plain=1#L93">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ESP32低功耗通用异步收发器（Low Power UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_lpcore.dtsi?plain=1#L103">已禁用：1</a>）</td>
<td><a href="../uart_espressif_infineon_microchip_binding_reference/P001_espressif_esp32-lpuart.md#std-dtcompatible-espressif-esp32-lpuart"><code>espressif,esp32-lpuart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/espressif/esp32c6/esp32c6_lpcore.dtsi?plain=1#L39">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
</table>

<a id="system-requirements"></a>

## 系统要求（System Requirements）

<a id="binary-blobs"></a>

### 二进制组件（Binary Blobs）

Espressif 硬件抽象层（HAL）需要射频（RF）二进制组件才能工作。运行下面的命令获取这些文件。

```text
west blobs fetch hal_espressif
```

注意（Note）

建议在 `west update` 之后运行上述命令。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`arduino_nesso_n1`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>esp32</td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd"><code>openocd</code></a></td>
<td>✅</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

<a id="simple-boot"></a>

### 简单启动（Simple Boot）

可以通过单一二进制镜像加载开发板，无需第二阶段引导加载程序（2nd-Stage Bootloader）。构建应用时没有附加配置，默认使用此方式。

注意（Note）

简单启动不提供安全功能，也不提供空中更新（Over-the-Air，OTA）。

<a id="mcuboot-bootloader"></a>

### MCUboot 引导加载程序（MCUboot Bootloader）

也可选择 MCUboot；此时必须至少构建并烧录一次引导加载程序。

构建应用有两种选择：


1. 系统构建（Sysbuild）
2. 手动构建（Manual Build）

注意（Note）

在开发板默认配置文件加入下面一行即可选择 MCUboot 引导加载程序。

```text
CONFIG_BOOTLOADER_MCUBOOT=y
```

<a id="sysbuild"></a>

### 系统构建（Sysbuild）

Sysbuild 可以统一构建并烧录启动 ESP32 SoC 开发板所需的全部镜像。

使用 Sysbuild 构建示例应用的命令如下：

```text
west build -b <board> --sysbuild samples/hello_world
```

默认情况下，ESP32 Sysbuild 生成引导加载程序（MCUboot）与应用镜像；也可配置为生成其他类型的镜像。

Sysbuild 生成的构建目录结构与传统 Zephyr 构建不同，输出按域（Domain）子目录组织：

```text
build/
├── hello_world
│   └── zephyr
│       ├── zephyr.elf
│       └── zephyr.bin
├── mcuboot
│    └── zephyr
│       ├── zephyr.elf
│       └── zephyr.bin
└── domains.yaml
```

注意（Note）

使用 `--sysbuild` 时，每次执行全新构建（Pristine Build）都会重新构建并重新烧录引导加载程序。

系统构建的更多信息见 Sysbuild（System Build）文档。（[系统构建（Sysbuild / System Build）](../sysbuild/P001_系统构建.md#sysbuild)）

<a id="manual-build"></a>

### 手动构建（Manual Build）

开发期间通常希望尽可能快地构建和烧录，因此可采用传统构建方式，每次只构建一个镜像。

以下说明同时适用于手动构建与 Sysbuild，区别仅在构建目录结构。

注意（Note）

请记住，必须至少烧录一次 MCUboot 引导加载程序。

按通常方式构建并烧录应用，详见“构建应用”（[Building an Application](../application/P001_应用开发.md#build-an-application)）与“运行应用”（[Run an Application](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)）。

```text
# From the root of the zephyr repository
west build -b <board> samples/hello_world
```

常规 `flash` 目标适用于此开发板配置。下面以 [Hello World](../getting_started/P005_HelloWorld示例.md#hello_world) 应用为例。

```text
# From the root of the zephyr repository
west build -b <board> samples/hello_world
west flash
```

注意（Note）

对于提供内置 USB Serial/JTAG 控制器的目标，芯片在 `west flash` 后可能仍处于下载模式，直到重新断电上电才启动新镜像。遇到此情况，可在烧录时选择看门狗复位（Watchdog Reset），使芯片自行重新启动：

```text
west flash --reset-type watchdog-reset
```

<a id="faster-flashing"></a>

### 加快烧录（Faster Flashing）

`--esp-skip-flashed` 在设备上进行 MD5 校验；若闪存中的二进制文件与待烧录文件相同，就跳过写入，加快开发过程：

```text
west flash --esp-skip-flashed
```

`--esp-diff` 仅写入相对于上次烧录镜像发生变化的区域，可进一步加快重复烧录。它与本地缓存副本比较，而不读取设备；因此仅当自上次 `west flash` 以来，闪存未被其他工具、其他开发板或手动写操作修改时使用：

```text
west flash --esp-diff
```

可关闭进度输出，使日志更简洁，适合持续集成（CI）：

```text
west flash --esp-no-progress
```

使用以下命令打开串口监视器（Serial Monitor）：

```text
west espressif monitor
```

开发板自动复位并启动后，监视器应显示以下消息：

```text
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! <board>
```

<a id="board-variants-using-snippets"></a>

### 使用配置片段的开发板变型（Board Variants Using Snippets）

ESP32 开发板可搭配不同模块，组合不同的 SPI 闪存容量、伪静态随机存储器（PSRAM）容量及 PSRAM 模式。`snippets/espressif` 中的配置片段提供模块化方式，在构建时应用这些差异，无需复制开发板定义。

支持以下基于配置片段的变型：

<table>
<tr>
<th>配置片段名称（Snippet Name）</th>
<th>说明（Description）</th>
</tr>
<tr>
<td colspan="2">闪存容量（Flash Memory Size）</td>
</tr>
<tr>
<td><code>espressif-flash-4M</code></td>
<td>配备 4 MB 闪存的开发板。</td>
</tr>
<tr>
<td><code>espressif-flash-8M</code></td>
<td>配备 8 MB 闪存的开发板。</td>
</tr>
<tr>
<td><code>espressif-flash-16M</code></td>
<td>配备 16 MB 闪存的开发板。</td>
</tr>
<tr>
<td><code>espressif-flash-32M</code></td>
<td>配备 32 MB 闪存的开发板。</td>
</tr>
<tr>
<td><code>espressif-flash-64M</code></td>
<td>配备 64 MB 闪存的开发板。</td>
</tr>
<tr>
<td><code>espressif-flash-128M</code></td>
<td>配备 128 MB 闪存的开发板。</td>
</tr>
<tr>
<td colspan="2">PSRAM 容量（PSRAM Memory Size）</td>
</tr>
<tr>
<td><code>espressif-psram-2M</code></td>
<td>配备 2 MB PSRAM 的开发板。</td>
</tr>
<tr>
<td><code>espressif-psram-4M</code></td>
<td>配备 4 MB PSRAM 的开发板。</td>
</tr>
<tr>
<td><code>espressif-psram-8M</code></td>
<td>配备 8 MB PSRAM 的开发板。</td>
</tr>
<tr>
<td colspan="2">PSRAM 用途（PSRAM Utilization）</td>
</tr>
<tr>
<td><code>espressif-psram-reloc</code></td>
<td>将闪存内容重定位（Relocate）到 PSRAM。</td>
</tr>
<tr>
<td><code>espressif-psram-wifi</code></td>
<td>将 Wi-Fi 缓冲区放入 PSRAM。</td>
</tr>
</table>

应用开发板变型时，在 `west build` 中使用 `-S` 参数：

```text
west build -b <board> -S espressif-flash-32M -S espressif-psram-4M samples/hello_world
```

注意（Note）

这些配置片段只适用于具有所选 Flash／PSRAM 配置对应硬件支持的开发板。


- 未选择 FLASH 配置片段时，使用开发板默认闪存容量。
- 未选择 PSRAM 配置片段时，使用开发板默认 PSRAM 容量。

<a id="debugging"></a>

### 调试（Debugging）

<a id="openocd-debugging"></a>

### OpenOCD 调试（OpenOCD Debugging）

<a id="id7"></a>

Espressif 芯片需要带 ESP32 专用补丁的自定义 OpenOCD 构建版本。请从 [OpenOCD for ESP32](https://github.com/espressif/openocd-esp32/releases) [注3](#id6) 下载最新发行版。

<a id="id11"></a>

详细的 JTAG 设置步骤见 ESP32 JTAG 调试文档 [注5](#id10)。（[ESP32的JTAG调试（JTAG Debugging）](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/index.html)）

<a id="zephyr-thread-awareness"></a>

#### Zephyr 线程感知（Zephyr Thread Awareness）

OpenOCD 支持 Zephyr RTOS 线程感知，使 GDB 能够：


- 使用 `info threads` 列出全部线程。
- 显示线程名称、优先级和状态。
- 在线程上下文（Thread Contexts）之间切换。
- 显示任意线程的调用栈回溯（Backtrace）。

要求（Requirements）：


- <a id="id9"></a>

  [OpenOCD ESP32 v0.12.0-esp32-20251215](https://github.com/espressif/openocd-esp32/releases/tag/v0.12.0-esp32-20251215) [注4](#id8) 或更高版本。
- 使用 `CONFIG_DEBUG_THREAD_INFO=y` 构建。

示例（Example）：

```text
# From the root of the zephyr repository
west build -b <board> samples/hello_world -- -DCONFIG_DEBUG_THREAD_INFO=y -DOPENOCD=<path/to/bin/openocd> -DOPENOCD_DEFAULT_PATH=<path/to/openocd/share/openocd/scripts>
west debug
```

<a id="using-a-custom-openocd"></a>

#### 使用自定义 OpenOCD（Using a Custom OpenOCD）

Zephyr SDK 自带 OpenOCD，但该版本可能不支持 ESP32。要使用 Espressif OpenOCD，需在构建时指定其路径：

```text
# From the root of the zephyr repository
west build -b <board> samples/hello_world -- -DOPENOCD=/path/to/openocd -DOPENOCD_DEFAULT_PATH=/path/to/openocd/scripts
west debug
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.espressif.com/sites/default/files/documentation/esp32-c6_datasheet_en.pdf](https://www.espressif.com/sites/default/files/documentation/esp32-c6_datasheet_en.pdf)

<a id="id4"></a>

〔[2](#id5)〕 [https://espressif.com/sites/default/files/documentation/esp32-c6_technical_reference_manual_en.pdf](https://espressif.com/sites/default/files/documentation/esp32-c6_technical_reference_manual_en.pdf)

<a id="id6"></a>

〔[3](#id7)〕 [https://github.com/espressif/openocd-esp32/releases](https://github.com/espressif/openocd-esp32/releases)

<a id="id8"></a>

〔[4](#id9)〕 [https://github.com/espressif/openocd-esp32/releases/tag/v0.12.0-esp32-20251215](https://github.com/espressif/openocd-esp32/releases/tag/v0.12.0-esp32-20251215)

<a id="id10"></a>

〔[5](#id11)〕 [https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/index.html](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/jtag-debugging/index.html)

<a id="id12"></a>

〔[6](#id13)〕 [https://docs.arduino.cc/hardware/nesso-n1/](https://docs.arduino.cc/hardware/nesso-n1/)

---

[上一章](P009_Arduino_Nano_R4.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_Arduino_Nicla_Sense_ME.md)
