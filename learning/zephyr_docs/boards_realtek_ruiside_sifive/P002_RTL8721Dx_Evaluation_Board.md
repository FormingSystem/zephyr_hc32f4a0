---
id: learning.zephyr-docs.boards-realtek-ruiside-sifive.page-2
title: RTL8721Dx Evaluation Board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/realtek/pke8721daf_c13_f10/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="pke8721daf_c13_f10"></a>

# 第2章\_RTL8721Dx评估板（Evaluation Board）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/realtek/pke8721daf_c13_f10/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/pke8721daf_c13_f10.webp](images/pke8721daf_c13_f10.webp)](images/pke8721daf_c13_f10.webp)

RTL8721Dx评估板（Evaluation Board）

名称（Name）：

`pke8721daf_c13_f10`

厂商（Vendor）：

[Realtek Semiconductor Corp.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=realtek)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[rtl8721dx](https://docs.zephyrproject.org/latest/boards/index.html#soc=rtl8721dx)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/realtek/pke8721daf_c13_f10/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id3"></a>

[PKE8721DAF-C13-F10](https://aiot.realmcu.com/zh/center/hardware/detail/56?theme_id=5)评估板基于Realtek RTL8721DAF-VT2-CG。该组合SoC支持双频Wi-Fi 4，即2.4 GHz及5 GHz，以及BLE 5.0。凭借超低功耗及丰富外设，可用于智能家电、线控器、智能门锁、电池摄像头、智能遥控器、Wi-Fi音箱、BLE网关及智能POS等。更多信息见PKE8721DAF-C13-F10 [注1](#id2)。

<a id="hardware"></a>

## 硬件（Hardware）

RTL8721DAF具有以下功能：


- 双核（Dual Cores）：


  - KM4最高运行频率345 MHz
  - KM0最高运行频率115 MHz
- 4 MB多芯片模块（MCM）闪存
- 512 KB片上SRAM
- 无线局域网（Wi-Fi）：


  - 802.11 a/b/g/n，1×1，2.4 GHz及5 GHz
  - 最高40 MHz带宽
- 蓝牙（Bluetooth）：


  - 低功耗蓝牙（BLE）5.0
  - 支持LE-1M、LE-2M及远距离LE-Coded物理层（PHY）
- 外设接口（Peripheral Interfaces）：


  - 4路UART，最高8 Mbit/s
  - 2路I2C，高速模式最高3.4 Mbit/s
  - 2路SPI，最高50 Mbit/s
  - 8通道脉宽调制（PWM）
  - 7+1通道12位模数转换器（ADC）
  - 4通道电容触摸（Cap-Touch）检测
  - 一路USB 2.0全速设备接口（Full-speed Device）
  - 一路SDIO设备接口，高速模式最高50 MHz
  - 一路红外（IR）接口

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`pke8721daf_c13_f10`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="pke8721daf_c13_f10-hw-features"></a>

<a id="pke8721daf_c13_f10-pke8721daf_c13_f10/rtl8721dx-hw-features-section"></a>

#### `pke8721daf_c13_f10/rtl8721dx`目标（Target）

<a id="pke8721daf_c13_f10-pke8721daf_c13_f10/rtl8721dx-hw-features-panel"></a>

<a id="pke8721daf_c13_f10-pke8721daf_c13_f10/rtl8721dx-hw-features-memory"></a>

该开发板目标的片上存储容量：192 KiB RAM、4 MiB Flash。

<a id="pke8721daf_c13_f10-pke8721daf_c13_f10/rtl8721dx-hw-features-table"></a>

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
<td>ARM Cortex-M55处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P003_arm_cortex-m55.md#std-dtcompatible-arm-cortex-m55"><code>arm,cortex-m55</code></a></td>
</tr>
<tr>
<td rowspan="1">模数转换器（ADC）</td>
<td>片上（On-Chip）</td>
<td>Ameba模数转换器（ADC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L181">已禁用：1</a>）</td>
<td><a href="../hardware/P895_RealtekAmeba模数转换器绑定.md#dtbinding-realtek-ameba-adc"><code>realtek,ameba-adc</code></a></td>
</tr>
<tr>
<td rowspan="1">蓝牙（Bluetooth）</td>
<td>片上（On-Chip）</td>
<td>Realtek Ameba蓝牙主机控制器接口（HCI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L322">已启用：1</a>）</td>
<td><a href="../bluetooth_vendor_hci_binding_reference/P010_realtek_ameba-bt-hci.md#std-dtcompatible-realtek-ameba-bt-hci"><code>realtek,ameba-bt-hci</code></a></td>
</tr>
<tr>
<td rowspan="2">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L36">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Ameba复位与时钟控制器节点（Reset and Clock Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L42">已启用：1</a>）</td>
<td><a href="../clock_nxp_pico_realtek_renesas_binding_reference/P021_realtek_ameba-rcc.md#std-dtcompatible-realtek-ameba-rcc"><code>realtek,ameba-rcc</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Ameba计数器（Counters）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L191">已禁用：10</a>）</td>
<td><a href="../renesas_realtek_counter_binding_reference/P009_realtek_ameba-counter.md#std-dtcompatible-realtek-ameba-counter"><code>realtek,ameba-counter</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Realtek通用直接存储器访问（GDMA）外设（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L73">已禁用：1</a>）</td>
<td><a href="../nxp_realtek_renesas_dma_binding_reference/P010_realtek_ameba-gdma.md#std-dtcompatible-realtek-ameba-gdma"><code>realtek,ameba-gdma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Ameba系列闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L106">已启用：1</a>）</td>
<td><a href="../flash_nuvoton_nxp_renesas_binding_reference/P022_realtek_ameba-flash-controller.md#std-dtcompatible-realtek-ameba-flash-controller"><code>realtek,ameba-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Realtek Ameba通用输入输出（GPIO）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L163">已启用：2</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P010_realtek_ameba-gpio.md#std-dtcompatible-realtek-ameba-gpio"><code>realtek,ameba-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Ameba I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L294">已禁用：2</a>）</td>
<td><a href="../i2c_nxp_pico_renesas_binding_reference/P009_realtek_ameba-i2c.md#std-dtcompatible-realtek-ameba-i2c"><code>realtek,ameba-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M嵌套向量中断控制器（NVIC / Nested Vectored Interrupt Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P004_ARMv8_1_M_NVIC.md#std-dtcompatible-arm-v8.1m-nvic"><code>arm,v8.1m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L115">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Realtek Ameba的pinctrl为单例节点（Singleton Node），负责引脚功能选择及属性控制。（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L131">已禁用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P002_realtek_ameba-pinctrl.md#std-dtcompatible-realtek-ameba-pinctrl"><code>realtek,ameba-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">脉宽调制（PWM）</td>
<td>片上（On-Chip）</td>
<td>Ameba脉宽调制（PWM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L264">已禁用：1</a>）</td>
<td><a href="../pwm_nxp_renesas_binding_reference/P015_realtek_ameba-pwm.md#std-dtcompatible-realtek-ameba-pwm"><code>realtek,ameba-pwm</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Ameba真随机数发生器（TRNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L124">已禁用：1</a>）</td>
<td><a href="../soc_rng_binding_reference/P002_realtek_ameba-trng.md#std-dtcompatible-realtek-ameba-trng"><code>realtek,ameba-trng</code></a></td>
</tr>
<tr>
<td rowspan="1">实时时钟（RTC）</td>
<td>片上（On-Chip）</td>
<td>Ameba实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L137">已禁用：1</a>）</td>
<td><a href="../soc_rtc_binding_reference/P004_realtek_ameba-rtc.md#std-dtcompatible-realtek-ameba-rtc"><code>realtek,ameba-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Ameba日志串口（LOGUART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L154">已启用：1</a>）</td>
<td><a href="../uart_raspberrypi_realtek_renesas_binding_reference/P003_realtek_ameba-loguart.md#std-dtcompatible-realtek-ameba-loguart"><code>realtek,ameba-loguart</code></a></td>
</tr>
<tr>
<td rowspan="1">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Ameba SPI控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L86">已禁用：2</a>）</td>
<td><a href="../spi_flexspi_nxp_renesas_binding_reference/P011_realtek_ameba-spi.md#std-dtcompatible-realtek-ameba-spi"><code>realtek,ameba-spi</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv8.1-M系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P008_ARMv8_1_M_SysTick.md#std-dtcompatible-arm-armv8.1m-systick"><code>arm,armv8.1m-systick</code></a></td>
</tr>
<tr>
<td rowspan="1">看门狗（Watchdog）</td>
<td>片上（On-Chip）</td>
<td>Ameba看门狗（Watchdog）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L146">已禁用：1</a>）</td>
<td><a href="../realtek_renesas_silabs_watchdog_binding_reference/P001_realtek_ameba-watchdog.md#std-dtcompatible-realtek-ameba-watchdog"><code>realtek,ameba-watchdog</code></a></td>
</tr>
<tr>
<td rowspan="1">无线局域网（Wi-Fi）</td>
<td>片上（On-Chip）</td>
<td>Realtek Ameba SoC的Wi-Fi功能（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/amebadplus/amebadplus.dtsi?plain=1#L61">已禁用：2</a>）</td>
<td><a href="../wifi_nordic_nxp_simulation_binding_reference/P011_realtek_ameba-wifi.md#std-dtcompatible-realtek-ameba-wifi"><code>realtek,ameba-wifi</code></a></td>
</tr>
</table>

<a id="system-requirements"></a>

## 系统要求（System Requirements）

<a id="binary-blobs"></a>

### 二进制组件（Binary Blobs）

Realtek硬件抽象层（HAL）需要二进制文件（Blobs）才能工作，运行以下命令获取。

```text
west blobs fetch hal_realtek
```

注意（Note）

建议在 `west update` 之后运行上述命令。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`pke8721daf_c13_f10`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td>amebaflash</td>
<td>✅（默认 / default）</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-jlink">jlink</a></td>
<td>✅</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>

<a id="building"></a>

### 构建（Building）

以下为构建[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用的示例：

```text
# From the root of the zephyr repository
west build -b pke8721daf_c13_f10 samples/hello_world
```

<a id="flashing"></a>

### 烧录（Flashing）

板级配置支持标准flash目标。

进入下载模式（Download Mode）

烧录前，需利用板载USB转UART转换器使SoC进入下载模式，步骤如下：


1. USB连接：将USB线缆连接到USB2UART端口。
2. 进入下载模式（Download Mode）：


  - 按住Download下载按键。
  - 保持按住Download，同时短按Chip_En使SoC复位。
  - 复位后松开Download。

此时SoC处于下载模式，可以接收固件。

注意（Note）

烧录命令中的<port_name>必须替换为实际串口，例如Linux下的/dev/ttyUSB0或Windows下的COM3。

以下为烧录[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)应用的示例：

```text
# From the root of the zephyr repository
west build -b pke8721daf_c13_f10 samples/hello_world
west flash --port <port_name>
```

进入正常模式（Normal Mode）

烧录成功后，按一次Chip_En重启SoC。设备随后进入正常模式并执行已烧录的Zephyr固件。

<a id="debugging"></a>

### 调试（Debugging）

可通过SWD使用J-Link调试探针，将其连接到PA30（SWD_CLK）及PA31（SWD_DAT）。以下为[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)的调试命令示例：

```text
# From the root of the zephyr repository
west build -b pke8721daf_c13_f10 samples/hello_world
west debug
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://aiot.realmcu.com/zh/center/hardware/detail/56?theme_id=5](https://aiot.realmcu.com/zh/center/hardware/detail/56?theme_id=5)

## 译注

PKE8721DAF-C13-F10与RTL872XDA-EVB同属RTL8721Dx，但板级标识不同。硬件512 KB SRAM与目标表192 KiB RAM分别保留；SWD为PA30／PA31。

---

[上一章](P001_Realtek.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_RTL8721F_Evaluation_Board.md)
