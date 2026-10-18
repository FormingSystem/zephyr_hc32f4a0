---
id: learning.zephyr-docs.boards-adafruit-feather-and-grand-central.page-8
title: RP2040 Scorpio Feather
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/adafruit/feather_scorpio_rp2040/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit_feather_scorpio_rp2040"></a>

# 第8章\_RP2040 Scorpio Feather

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/adafruit/feather_scorpio_rp2040/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/adafruit_feather_scorpio_rp2040.webp](images/adafruit_feather_scorpio_rp2040.webp)](images/adafruit_feather_scorpio_rp2040.webp)

RP2040 Scorpio Feather

名称（Name）：

`adafruit_feather_scorpio_rp2040`

厂商（Vendor）：

[Adafruit Industries, LLC](https://docs.zephyrproject.org/latest/boards/index.html#vendor=adafruit)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[rp2040](https://docs.zephyrproject.org/latest/boards/index.html#soc=rp2040)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adafruit/feather_scorpio_rp2040/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id3"></a>

[Adafruit RP2040 Scorpio Feather](https://learn.adafruit.com/introducing-feather-rp2040-scorpio)[注1](#id2)开发板采用Raspberry Pi Ltd.的RP2040微控制器（Microcontroller）。它提供8路外部RGB LED（NeoPixel）输出，以及便于连接传感器的STEMMA QT接口。它兼容Feather开发板外形规格（Form Factor），并配有USB Type-C接口。

<a id="hardware"></a>

## 硬件（Hardware）


- Raspberry Pi RP2040微控制器（Microcontroller），最高频率133 MHz
- 双ARM Cortex-M0+内核
- 264 kByte静态随机存储器（SRAM）
- 8 Mbyte四线SPI闪存（QSPI Flash）
- 25个通用输入输出（GPIO）引脚
- 4个模数转换器（ADC）引脚
- 集成电路间总线（I2C）
- 串行外设接口（SPI）
- 通用异步收发器（UART）
- USB Type-C接口
- 复位和启动按键（Reset / Boot Buttons）
- 板载红色LED（Red LED）
- 板载RGB LED（NeoPixel）
- STEMMA QT I2C接口，也称Qwiic
- 内置锂离子电池充电器（Lithium-ion Battery Charger）
- 8路外部NeoPixel输出

<a id="default-zephyr-peripheral-mapping"></a>

### Zephyr默认外设映射（Default Peripheral Mapping）

<table>
<tr>
<th>说明（Description）</th>
<th>引脚（Pin）</th>
<th>默认引脚复用（Default Pin Mux）</th>
<th>备注（Comment）</th>
</tr>
<tr>
<td>启动按键（Boot Button）</td>
<td>GPIO7</td>
<td></td>
<td>别名（Alias）<code>sw0</code></td>
</tr>
</table>

Feather排针（Header）：

<table>
<tr>
<th>标签（Label）</th>
<th>引脚（Pin）</th>
<th>默认引脚复用（Default Pin Mux）</th>
<th>同时用于（Also Used In）</th>
</tr>
<tr>
<td>A0</td>
<td>GPIO26</td>
<td>ADC0</td>
<td></td>
</tr>
<tr>
<td>A1</td>
<td>GPIO27</td>
<td>ADC1</td>
<td></td>
</tr>
<tr>
<td>A2</td>
<td>GPIO28</td>
<td>ADC2</td>
<td></td>
</tr>
<tr>
<td>A3</td>
<td>GPIO29</td>
<td>ADC3</td>
<td></td>
</tr>
<tr>
<td>24</td>
<td>GPIO24</td>
<td></td>
<td></td>
</tr>
<tr>
<td>25</td>
<td>GPIO25</td>
<td></td>
<td></td>
</tr>
<tr>
<td>SCK</td>
<td>GPIO14</td>
<td>SPI1时钟（SCK）</td>
<td></td>
</tr>
<tr>
<td>MO</td>
<td>GPIO15</td>
<td>SPI1主机输出从机输入（MOSI）</td>
<td></td>
</tr>
<tr>
<td>MI</td>
<td>GPIO8</td>
<td>SPI1主机输入从机输出（MISO）</td>
<td></td>
</tr>
<tr>
<td>R</td>
<td>GPIO1</td>
<td>UART0接收（RX）</td>
<td></td>
</tr>
<tr>
<td>T</td>
<td>GPIO0</td>
<td>UART0发送（TX）</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>GPIO4</td>
<td>PIO0</td>
<td>板载NeoPixel（On-board NeoPixel）</td>
</tr>
<tr>
<td>D</td>
<td>GPIO2</td>
<td>I2C1数据（SDA）</td>
<td>STEMMA QT</td>
</tr>
<tr>
<td>C</td>
<td>GPIO3</td>
<td>I2C1时钟（SCL）</td>
<td>STEMMA QT</td>
</tr>
<tr>
<td>5</td>
<td>GPIO5</td>
<td></td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>GPIO6</td>
<td></td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>GPIO9</td>
<td></td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>GPIO10</td>
<td></td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>GPIO11</td>
<td></td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>GPIO12</td>
<td></td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>GPIO13</td>
<td></td>
<td>红色用户LED（Red User LED）</td>
</tr>
</table>

STEMMA QT I2C接口，其引脚也在Feather排针上引出：

<table>
<tr>
<th>标签（Label）</th>
<th>引脚（Pin）</th>
<th>默认引脚复用（Default Pin Mux）</th>
</tr>
<tr>
<td>SDA</td>
<td>GPIO2</td>
<td>I2C1数据（SDA）</td>
</tr>
<tr>
<td>SCL</td>
<td>GPIO3</td>
<td>I2C1时钟（SCL）</td>
</tr>
</table>

外部NeoPixel排针（Header）：

<table>
<tr>
<th>标签（Label）</th>
<th>引脚（Pin）</th>
<th>默认引脚复用（Default Pin Mux）</th>
</tr>
<tr>
<td>0</td>
<td>GPIO16</td>
<td>PIO1</td>
</tr>
<tr>
<td>1</td>
<td>GPIO17</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>GPIO18</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>GPIO19</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>GPIO20</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>GPIO21</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>GPIO22</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>GPIO23</td>
<td></td>
</tr>
</table>

<a id="id5"></a>

<a id="id7"></a>

另请参阅[引脚分配（Pinout）](https://learn.adafruit.com/introducing-feather-rp2040-scorpio/pinouts)[注2](#id4)和[原理图（Schematic）](https://learn.adafruit.com/introducing-feather-rp2040-scorpio/downloads)[注3](#id6)。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`adafruit_feather_scorpio_rp2040`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="adafruit_feather_scorpio_rp2040-hw-features"></a>

<a id="adafruit_feather_scorpio_rp2040-adafruit_feather_scorpio_rp2040/rp2040-hw-features-section"></a>

#### `adafruit_feather_scorpio_rp2040/rp2040`目标（Target）

<a id="adafruit_feather_scorpio_rp2040-adafruit_feather_scorpio_rp2040/rp2040-hw-features-panel"></a>

<a id="adafruit_feather_scorpio_rp2040-adafruit_feather_scorpio_rp2040/rp2040-hw-features-memory"></a>

该开发板目标的片上存储容量：264 KiB RAM、8 MiB Flash。

<a id="adafruit_feather_scorpio_rp2040-adafruit_feather_scorpio_rp2040/rp2040-hw-features-table"></a>

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
<td>ARM Cortex-M0+处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L35">已启用：2</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P017_arm_cortex-m0+.md#std-dtcompatible-arm-cortex-m0"><code>arm,cortex-m0+</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L309">已启用：1</a>）</td>
<td><a href="../hardware/P894_RaspberryPiPico模数转换器绑定.md#dtbinding-raspberrypi-pico-adc"><code>raspberrypi,pico-adc</code></a></td>
</tr>
<tr>
<td rowspan="5">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico时钟控制器（Clock Controller）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L220">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P016_raspberrypi_pico-clock-controller.md#std-dtcompatible-raspberrypi-pico-clock-controller"><code>raspberrypi,pico-clock-controller</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico时钟（Clock）的表示（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L47">已启用：11</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L174">已禁用：2</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P017_raspberrypi_pico-clock.md#std-dtcompatible-raspberrypi-pico-clock"><code>raspberrypi,pico-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico锁相环（PLL）的表示（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L128">已启用：2</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P018_raspberrypi_pico-pll.md#std-dtcompatible-raspberrypi-pico-pll"><code>raspberrypi,pico-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico环形振荡器（Ring Oscillator）的表示（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L150">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P019_raspberrypi_pico-rosc.md#std-dtcompatible-raspberrypi-pico-rosc"><code>raspberrypi,pico-rosc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico外部振荡器（External Oscillator）的表示（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L168">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P020_raspberrypi_pico-xosc.md#std-dtcompatible-raspberrypi-pico-xosc"><code>raspberrypi,pico-xosc</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico定时器（Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L373">已启用：1</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P008_raspberrypi_pico-timer.md#std-dtcompatible-raspberrypi-pico-timer"><code>raspberrypi,pico-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico直接存储器访问（DMA）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L389">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P009_raspberrypi_pico-dma.md#std-dtcompatible-raspberrypi-pico-dma"><code>raspberrypi,pico-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico闪存控制器（Flash Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L197">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P021_raspberrypi_pico-flash-controller.md#std-dtcompatible-raspberrypi-pico-flash-controller"><code>raspberrypi,pico-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="4">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L242">已启用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P006_raspberrypi_pico-gpio.md#std-dtcompatible-raspberrypi-pico-gpio"><code>raspberrypi,pico-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico GPIO端口（Port）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L255">已启用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P005_raspberrypi_pico-gpio-port.md#std-dtcompatible-raspberrypi-pico-gpio-port"><code>raspberrypi,pico-gpio-port</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>引出到Adafruit Feather排针（Headers）的GPIO引脚（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/feather_scorpio_rp2040/feather_connector.dtsi?plain=1#L8">已启用：1</a>）</td>
<td><a href="../gpio_adi_headers_ambiq_binding_reference/P001_adafruit-feather-header.md#std-dtcompatible-adafruit-feather-header"><code>adafruit-feather-header</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>STEMMA QT是一种用于I2C设备的4针JST-SH接口。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/feather_scorpio_rp2040/adafruit_feather_scorpio_rp2040.dts?plain=1#L61">已启用：1</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P005_stemma-qt-connector.md#std-dtcompatible-stemma-qt-connector"><code>stemma-qt-connector</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L332">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L320">已禁用：1</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P008_raspberrypi_pico-i2c.md#std-dtcompatible-raspberrypi-pico-i2c"><code>raspberrypi,pico-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/feather_scorpio_rp2040/adafruit_feather_scorpio_rp2040.dts?plain=1#L51">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic"><code>arm,v6m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/feather_scorpio_rp2040/adafruit_feather_scorpio_rp2040.dts?plain=1#L42">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">灯带（LED Strip）</td>
<td>板载（On-Board）</td>
<td>配置用于WS2812的可编程输入输出（PIO）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/feather_scorpio_rp2040/adafruit_feather_scorpio_rp2040.dts?plain=1#L180">已启用：2</a>）</td>
<td><a href="../led_strip_binding_reference/P011_worldsemi_ws2812-rpi_pico-pio.md#std-dtcompatible-worldsemi-ws2812-rpi_pico-pio"><code>worldsemi,ws2812-rpi_pico-pio</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico处理器间邮箱（Interprocessor Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L452">已禁用：2</a>）</td>
<td><a href="../intercore_reference/P050_Pico邮箱绑定.md#dtbinding-raspberrypi-pico-mbox"><code>raspberrypi,pico-mbox</code></a></td>
</tr>
<tr>
<td rowspan="2">其他绑定（Miscellaneous）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico可编程输入输出（PIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L412">已启用：2</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P011_raspberrypi_pico-pio.md#std-dtcompatible-raspberrypi-pico-pio"><code>raspberrypi,pico-pio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico单周期输入输出（SIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L444">已启用：1</a>）</td>
<td><a href="../misc_nxp_renesas_zephyr_binding_reference/P013_raspberrypi_pico-sio.md#std-dtcompatible-raspberrypi-pico-sio"><code>raspberrypi,pico-sio</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L205">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L492">已启用：1</a>）</td>
<td><a href="../pinctrl_nxp_pico_binding_reference/P025_raspberrypi_pico-pinctrl.md#std-dtcompatible-raspberrypi-pico-pinctrl"><code>raspberrypi,pico-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L362">已启用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P014_raspberrypi_pico-pwm.md#std-dtcompatible-raspberrypi-pico-pwm"><code>raspberrypi,pico-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">稳压器（Regulator）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico内核电源稳压器（Core Supply Regulator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L402">已启用：1</a>）</td>
<td><a href="../hardware/P654_RaspberryPi内核供电稳压器绑定.md#dtbinding-raspberrypi-core-supply-regulator"><code>raspberrypi,core-supply-regulator</code></a></td>
</tr>
<tr>
<td rowspan="1">复位控制器（Reset Controller）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico复位控制器（Reset Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L214">已启用：1</a>）</td>
<td><a href="../reset_controller_binding_reference/P012_raspberrypi_pico-reset.md#std-dtcompatible-raspberrypi-pico-reset"><code>raspberrypi,pico-reset</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L434">已禁用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P003_raspberrypi_pico-rtc.md#std-dtcompatible-raspberrypi-pico-rtc"><code>raspberrypi,pico-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico系列温度传感器（Temperature Sensor）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L496">已启用：1</a>）</td>
<td><a href="../sensor_realtek_rohm_sensirion_binding_reference/P003_raspberrypi_pico-temp.md#std-dtcompatible-raspberrypi-pico-temp"><code>raspberrypi,pico-temp</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L265">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L275">已禁用：1</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P002_raspberrypi_pico-uart.md#std-dtcompatible-raspberrypi-pico-uart"><code>raspberrypi,pico-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico串行外设接口（SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L297">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L285">已禁用：1</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P010_raspberrypi_pico-spi.md#std-dtcompatible-raspberrypi-pico-spi"><code>raspberrypi,pico-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L192">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv6-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P005_ARMv6_M_SysTick.md#std-dtcompatible-arm-armv6m-systick"><code>arm,armv6m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico USB设备控制器（USB Device Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L351">已启用：1</a>）</td>
<td><a href="../usb_soc_binding_reference/P014_raspberrypi_pico-usbd.md#std-dtcompatible-raspberrypi-pico-usbd"><code>raspberrypi,pico-usbd</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Raspberry Pi Pico看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/raspberrypi/rpi_pico/rp2040.dtsi?plain=1#L344">已启用：1</a>）</td>
<td><a href="../nxp_nordic_nuvoton_watchdog_binding_reference/P015_raspberrypi_pico-watchdog.md#std-dtcompatible-raspberrypi-pico-watchdog"><code>raspberrypi,pico-watchdog</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`adafruit_feather_scorpio_rp2040`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>连接调试会话（attach）</th>
<th>rtt</th>
<th>debugserver</th>
<th>reset</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-blackmagicprobe">blackmagicprobe</a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td></td>
<td></td>
<td></td>
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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-uf2">uf2</a></td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

默认通过USB接口编程。按住BOOT按键，再按RST按键，设备便会显示为USB大容量存储设备（USB Mass Storage Unit）。构建应用后会生成`build/zephyr/zephyr.uf2`文件，将该文件拖放到USB存储设备中，即可重新编程开发板。

也可以通过SWDIO和SWCLK引脚进行编程和调试。此时需要独立的硬件编程工具，并使用OpenOCD等软件。通常应在构建时设置`OPENOCD`和`OPENOCD_DEFAULT_PATH`，烧录时使用`--runner openocd`参数。有关RP2040开发板编程的更多信息，请参阅编程与调试（[Programming and Debugging](https://docs.zephyrproject.org/latest/boards/raspberrypi/rpi_pico/doc/index.html#rpi-pico-programming-and-debugging)）。

<a id="flashing"></a>

### 烧录（Flashing）

运行闪灯（[Blinky](../getting_started/P004_LED闪烁示例.md#blinky)）示例：

```text
# From the root of the zephyr repository
west build -b adafruit_feather_scorpio_rp2040 samples/basic/blinky/
west flash
```

还可以尝试LED[灯带（LED Strip）](../hardware/P191_LED灯带示例.md#led-strip)、[输入事件转储（Input Dump）](../interaction/P014_输入事件转储示例.md#input-dump)、[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)以及[使用设备树的模数转换器（ADC with Devicetree）](../hardware/P439_ADC设备树示例.md#adc_dt)示例。

由于按键所连接的线路也用于QSPI存储器，按键（[Button](../basic_samples/P003_按钮输入.md#button)）示例可能报告虚假的按键按下事件（Spurious Button Presses）。

下面使用[通用光照传感器轮询（Generic Light Sensor Polling）](../sensors/P019_光照传感器轮询示例.md#light_sensor_polling)示例和单独的扩展板（Shield），演示STEMMA QT I2C接口的使用：

```text
# From the root of the zephyr repository
west build -b adafruit_feather_scorpio_rp2040 --shield adafruit_veml7700 samples/sensor/light_polling/
west flash
```

作为通过板边排针使用外部NeoPixel的示例，设备树描述了一串连接到输出0的NeoPixel。需要将`external_ws2812`节点中的像素数量改为外部灯带的实际数量，还必须将`aliases`属性中的`led-strip = &onboard_ws2812;`改为`led-strip = &external_ws2812;`，然后运行LED[灯带（LED Strip）](../hardware/P191_LED灯带示例.md#led-strip)示例。

以类似方式调整设备树文件，也可以为其他外部输出引脚启用NeoPixel驱动。

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://learn.adafruit.com/introducing-feather-rp2040-scorpio](https://learn.adafruit.com/introducing-feather-rp2040-scorpio)

<a id="id4"></a>

〔[2](#id5)〕 [https://learn.adafruit.com/introducing-feather-rp2040-scorpio/pinouts](https://learn.adafruit.com/introducing-feather-rp2040-scorpio/pinouts)

<a id="id6"></a>

〔[3](#id7)〕 [https://learn.adafruit.com/introducing-feather-rp2040-scorpio/downloads](https://learn.adafruit.com/introducing-feather-rp2040-scorpio/downloads)

---

[上一章](P007_Feather_RP2040.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_Feather_STM32F405_Express.md)
