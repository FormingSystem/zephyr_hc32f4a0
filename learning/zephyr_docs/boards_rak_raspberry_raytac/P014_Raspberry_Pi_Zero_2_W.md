---
id: learning.zephyr-docs.boards-rak-raspberry-raytac.page-14
title: Raspberry Pi Zero 2 W
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/raspberrypi/rpi_zero_2w/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="rpi_zero_2w"></a>

# 第14章\_Raspberry Pi Zero 2 W

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/raspberrypi/rpi_zero_2w/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`rpi_zero_2w`

厂商（Vendor）：

[Raspberry Pi基金会（Foundation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=raspberrypi)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[bcm2710](https://docs.zephyrproject.org/latest/boards/index.html#soc=bcm2710)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/raspberrypi/rpi_zero_2w/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id2"></a>

[Raspberry Pi Zero 2 W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) [注1](#id1)是一款小型单板计算机，基于Broadcom BCM2710A1 SoC，与初代Raspberry Pi 3采用相同芯片。它与512 MB LPDDR2 SDRAM一起封装于RP3A0-AU系统级封装（SiP）内。

<a id="id8"></a>

<a id="id6"></a>

Zephyr以单核模式运行BCM2710A1。由于此SoC没有通用中断控制器（GIC），Zephyr直接使用BCM2836 ARM本地中断控制器，见[QA7 ARM Quad-A7 Core](https://datasheets.raspberrypi.com/bcm2836/QA7_rev3.4.pdf) [注4](#id7)，以及BCM2835 ARMC外设中断控制器，见[BCM2837 ARM Peripherals](https://datasheets.raspberrypi.com/bcm2837/bcm2837-peripherals.pdf) [注3](#id5)。默认控制台是GPIO 14／15上的mini-UART。

<a id="hardware"></a>

## 硬件（Hardware）


- 1 GHz四核64位Arm Cortex-A53 CPU
- 512 MB同步动态RAM（SDRAM）
- 2.4 GHz 802.11 b/g/n无线局域网（WLAN）
- Bluetooth 4.2、低功耗蓝牙（BLE）及板载天线
- Mini-HDMI端口及Micro-USB OTG端口
- microSD卡槽（Card Slot）
- CSI-2摄像头连接器
- 兼容HAT的40引脚排针焊盘，默认未装排针
- H.264及MPEG-4解码，1080p30；H.264编码，1080p30
- OpenGL ES 1.1及2.0图形支持
- Micro-USB供电
- 通过焊接测试点引出复合视频及复位引脚

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`rpi_zero_2w`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="rpi_zero_2w-hw-features"></a>

<a id="rpi_zero_2w-rpi_zero_2w/bcm2710-hw-features-section"></a>

#### `rpi_zero_2w/bcm2710`目标（Target）

<a id="rpi_zero_2w-rpi_zero_2w/bcm2710-hw-features-panel"></a>

<a id="rpi_zero_2w-rpi_zero_2w/bcm2710-hw-features-memory"></a>

该开发板目标的片上存储容量：256 MiB RAM、N/A Flash。

<a id="rpi_zero_2w-rpi_zero_2w/bcm2710-hw-features-table"></a>

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
<td>ARM Cortex-A53处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2710.dtsi?plain=1#L27">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P008_arm_cortex-a53.md#std-dtcompatible-arm-cortex-a53"><code>arm,cortex-a53</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2710.dtsi?plain=1#L49">已启用：2</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">固件（Firmware）</td>
<td>板载（On-Board）</td>
<td>Raspberry Pi固件接口（Firmware Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_zero_2w/rpi_zero_2w.dts?plain=1#L56">已启用：1</a>）</td>
<td><a href="../hardware/P611_BCM283x固件绑定.md#dtbinding-raspberrypi-bcm283x-firmware"><code>raspberrypi,bcm283x-firmware</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>BCM2711通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2710.dtsi?plain=1#L95">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2710.dtsi?plain=1#L105">已禁用：1</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P007_brcm_bcm2711-gpio.md#std-dtcompatible-brcm-bcm2711-gpio"><code>brcm,bcm2711-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Broadcom BCM2711 I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2710.dtsi?plain=1#L147">已禁用：3</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P013_brcm_bcm2711-i2c.md#std-dtcompatible-brcm-bcm2711-i2c"><code>brcm,bcm2711-i2c</code></a></td>
</tr>
<tr>
<td rowspan="2">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>BCM2836／BCM2710 ARM本地中断控制器，适用于Pi 2、Pi 3及Pi Zero 2 W（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2710.dtsi?plain=1#L64">已启用：1</a>）</td>
<td><a href="../soc_interrupt_binding_reference/P004_brcm_bcm2836-l1-intc.md#std-dtcompatible-brcm-bcm2836-l1-intc"><code>brcm,bcm2836-l1-intc</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>BCM2835 ARMC外设中断控制器，即BCM283x系列中的GPU IRQ一侧，适用于Pi 1、Pi 2、Pi 3及Pi Zero系列（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2710.dtsi?plain=1#L72">已启用：1</a>）</td>
<td><a href="../soc_interrupt_binding_reference/P003_brcm_bcm2835-armctrl-ic.md#std-dtcompatible-brcm-bcm2835-armctrl-ic"><code>brcm,bcm2835-armctrl-ic</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>Broadcom BCM2711 VideoCore邮箱（Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2710.dtsi?plain=1#L134">已启用：1</a>）</td>
<td><a href="../intercore_reference/P036_BCM2711邮箱绑定.md#dtbinding-brcm-bcm2711-mbox"><code>brcm,bcm2711-mbox</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Broadcom BCM2711引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2710.dtsi?plain=1#L88">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P017_brcm_bcm2711-pinctrl.md#std-dtcompatible-brcm-bcm2711-pinctrl"><code>brcm,bcm2711-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Broadcom BCM2835随机数发生器（RNG）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2710.dtsi?plain=1#L82">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P005_brcm_bcm2835-rng.md#std-dtcompatible-brcm-bcm2835-rng"><code>brcm,bcm2835-rng</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>Raspberry Pi BCM283x SoC芯片温度传感器（Die-temperature Sensor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_zero_2w/rpi_zero_2w.dts?plain=1#L62">已启用：1</a>）</td>
<td><a href="../sensor_realtek_rohm_sensirion_binding_reference/P002_raspberrypi_bcm283x-vc-thermal.md#std-dtcompatible-raspberrypi-bcm283x-vc-thermal"><code>raspberrypi,bcm283x-vc-thermal</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM PL011通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2710.dtsi?plain=1#L116">已禁用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011"><code>arm,pl011</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Broadcom BCM283x辅助UART（Auxiliary UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2710.dtsi?plain=1#L125">已启用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P014_brcm_bcm283x-aux-uart.md#std-dtcompatible-brcm-bcm283x-aux-uart"><code>brcm,bcm283x-aux-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_zero_2w/rpi_zero_2w.dts?plain=1#L28">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2710.dtsi?plain=1#L38">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`rpi_zero_2w`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

<a id="microsd-card"></a>

### MicroSD存储卡

通过Raspberry Pi Imager将64位Raspberry Pi OS Lite镜像写入MicroSD卡。此过程会创建FAT启动分区，放入bootcode.bin、fixup.dat及start.elf等固件二进制文件，供BCM2710A1启动ARM核。

在该启动分区的根目录中：


1. 复制build/zephyr/zephyr.bin。
2. 将config.txt替换为以下内容：

  ```text
  arm_64bit=1
  enable_uart=1
  core_freq=250
  kernel_address=0x200000
  kernel=zephyr.bin
  ```

<a id="id4"></a>

<a id="id10"></a>

内核文件名不以kernel8开头时，必须设置arm_64bit=1。enable_uart=1将mini-UART路由至GPIO 14／15，否则这些引脚将由蓝牙无线电使用。core_freq=250锁定视频处理单元（VPU）时钟，保证mini-UART波特率除数有效；enable_uart=1本应隐含此设置，但并非始终如此，见[raspberrypi/linux问题#4123](https://github.com/raspberrypi/linux/issues/4123) [注2](#id3)。kernel_address必须与板级设备树中的DRAM基地址一致。完整固件选项见[config.txt参考资料](https://www.raspberrypi.com/documentation/computers/config_txt.html)[注5](#id9)。

弹出存储卡并启动Pi。控制台在mini-UART上以115200、8N1、无流控制启动：

```text
*** Booting Zephyr OS build v4.x.x-... ***
Hello World! rpi_zero_2w
```

<a id="console-connection"></a>

### 连接控制台（Console Connection）

将3.3 V USB转UART适配器连接到GPIO排针：

<table>
<tr>
<th>适配器（Adapter）</th>
<th>Pi排针引脚</th>
<th>Pi GPIO及功能</th>
</tr>
<tr>
<td>地（GND）</td>
<td>第6脚，或第9、14脚</td>
<td>地（GND）</td>
</tr>
<tr>
<td>接收（RX）</td>
<td>8</td>
<td>GPIO 14／mini-UART发送（TX）</td>
</tr>
<tr>
<td>发送（TX）</td>
<td>10</td>
<td>GPIO 15／mini-UART接收（RX）</td>
</tr>
</table>

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)

<a id="id3"></a>

〔[2](#id4)〕 [https://github.com/raspberrypi/linux/issues/4123](https://github.com/raspberrypi/linux/issues/4123)

<a id="id5"></a>

〔[3](#id6)〕 [https://datasheets.raspberrypi.com/bcm2837/bcm2837-peripherals.pdf](https://datasheets.raspberrypi.com/bcm2837/bcm2837-peripherals.pdf)

<a id="id7"></a>

〔[4](#id8)〕 [https://datasheets.raspberrypi.com/bcm2836/QA7_rev3.4.pdf](https://datasheets.raspberrypi.com/bcm2836/QA7_rev3.4.pdf)

<a id="id9"></a>

〔[5](#id10)〕 [https://www.raspberrypi.com/documentation/computers/config_txt.html](https://www.raspberrypi.com/documentation/computers/config_txt.html)

## 译注

Zero 2 W的SoC没有GIC，使用ARM本地及ARMC外设中断控制器，Zephyr单核运行。mini-UART的时钟锁定与DRAM基地址要求保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [QA7_rev3.4.pdf](https://datasheets.raspberrypi.com/bcm2836/QA7_rev3.4.pdf)：HTTP Error 404: Not Found。
- [bcm2837-peripherals.pdf](https://datasheets.raspberrypi.com/bcm2837/bcm2837-peripherals.pdf)：HTTP Error 404: Not Found。
- [config_txt.html](https://www.raspberrypi.com/documentation/computers/config_txt.html)：HTTP Error 403: Forbidden。
- [](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)：HTTP Error 403: Forbidden。

---

[上一章](P013_Raspberry_Pi_Pico_2.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P015_AN54LQ-DB-15.md)
