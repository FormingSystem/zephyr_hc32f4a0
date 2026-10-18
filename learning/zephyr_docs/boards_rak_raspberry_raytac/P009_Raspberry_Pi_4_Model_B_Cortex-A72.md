---
id: learning.zephyr-docs.boards-rak-raspberry-raytac.page-9
title: Raspberry Pi 4 Model B Cortex-A72
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/raspberrypi/rpi_4b/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="rpi_4b"></a>

# 第9章\_Raspberry Pi 4 Model B（Cortex-A72）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/raspberrypi/rpi_4b/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/rpi_4b.webp](images/rpi_4b.webp)](images/rpi_4b.webp)

Raspberry Pi 4 Model B（Cortex-A72）

名称（Name）：

`rpi_4b`

厂商（Vendor）：

[Raspberry Pi基金会（Foundation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=raspberrypi)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[bcm2711](https://docs.zephyrproject.org/latest/boards/index.html#soc=bcm2711)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/raspberrypi/rpi_4b/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id3"></a>

[Raspberry Pi 4](https://pip.raspberrypi.com/documents/RP-008344-DS-raspberry-pi-4-product-brief.pdf/) [注1](#id2)是Raspberry Pi旗舰系列的第四代单板计算机（Single-board Computer）。它基于Broadcom BCM2711 SoC，采用四核64位ARM Cortex-A72 CPU，提供1、2、4或8 GB LPDDR4 RAM配置。

<a id="hardware"></a>

## 硬件（Hardware）


- Broadcom BCM2711，四核64位Cortex-A72（ARMv8）SoC，1.8 GHz
- LPDDR4-3200同步动态RAM（SDRAM），容量依型号为1、2、4或8 GB
- 2.4 GHz及5.0 GHz IEEE 802.11ac无线连接、Bluetooth 5.0及低功耗蓝牙（BLE）
- 千兆以太网（Gigabit Ethernet）
- 两个USB 3.0端口及两个USB 2.0端口
- Raspberry Pi标准40引脚GPIO排针，完全向后兼容此前板卡
- 两个Micro-HDMI端口，最高支持4Kp60
- 双通道MIPI DSI显示接口
- 双通道MIPI CSI摄像头接口
- 四触点立体声音频及复合视频接口
- H.265：4Kp60解码；H.264：1080p60解码、1080p30编码
- OpenGL ES 3.1及Vulkan 1.0
- MicroSD卡槽，用于加载操作系统及存储数据
- 通过USB-C输入5 V直流电源，至少3 A
- 通过GPIO排针输入5 V直流电源，至少3 A
- 支持以太网供电（PoE），需另配PoE HAT扩展板

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`rpi_4b`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="rpi_4b-hw-features"></a>

<a id="rpi_4b-rpi_4b/bcm2711-hw-features-section"></a>

#### `rpi_4b/bcm2711`目标（Target）

<a id="rpi_4b-rpi_4b/bcm2711-hw-features-panel"></a>

<a id="rpi_4b-rpi_4b/bcm2711-hw-features-memory"></a>

该开发板目标的片上存储容量：8 MiB RAM、N/A Flash。

<a id="rpi_4b-rpi_4b/bcm2711-hw-features-table"></a>

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
<td>ARM Cortex-A72处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L23">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P012_arm_cortex-a72.md#std-dtcompatible-arm-cortex-a72"><code>arm,cortex-a72</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L67">已启用：2</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">显示（Display）</td>
<td>板载（On-Board）</td>
<td>Raspberry Pi BCM2711帧缓冲（Framebuffer）显示设备（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L94">已启用：1</a>）</td>
<td><a href="../display_panel_renesas_sharp_binding_reference/P006_raspberrypi_bcm2711-framebuffer.md#std-dtcompatible-raspberrypi-bcm2711-framebuffer"><code>raspberrypi,bcm2711-framebuffer</code></a></td>
</tr>
<tr>
<td rowspan="3">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Broadcom GENET千兆以太网控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L293">已启用：1</a>）</td>
<td><a href="../ethernet_mac_mdio_binding_reference/P006_brcm_genet.md#std-dtcompatible-brcm-genet"><code>brcm,genet</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Broadcom GENET管理数据输入输出（MDIO）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L302">已启用：1</a>）</td>
<td><a href="../ethernet_mac_mdio_binding_reference/P017_brcm_genet-mdio.md#std-dtcompatible-brcm-genet-mdio"><code>brcm,genet-mdio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>通用媒体独立接口物理层（MII PHY）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L152">已启用：1</a>）</td>
<td><a href="../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy"><code>ethernet-phy</code></a></td>
</tr>
<tr>
<td rowspan="1">固件（Firmware）</td>
<td>板载（On-Board）</td>
<td>Raspberry Pi固件接口（Firmware Interface）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L75">已启用：1</a>）</td>
<td><a href="../hardware/P611_BCM283x固件绑定.md#dtbinding-raspberrypi-bcm283x-firmware"><code>raspberrypi,bcm283x-firmware</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>BCM2711通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L134">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L122">已禁用：1</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P007_brcm_bcm2711-gpio.md#std-dtcompatible-brcm-bcm2711-gpio"><code>brcm,bcm2711-gpio</code></a></td>
</tr>
<tr>
<td>板载（On-Board）</td>
<td>Raspberry Pi BCM283x GPIO扩展器（Expander）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L81">已启用：1</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P003_raspberrypi_bcm283x-gpio.md#std-dtcompatible-raspberrypi-bcm283x-gpio"><code>raspberrypi,bcm283x-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Broadcom BCM2711 I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L217">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L206">已禁用：5</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P013_brcm_bcm2711-i2c.md#std-dtcompatible-brcm-bcm2711-i2c"><code>brcm,bcm2711-i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v2（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L89">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P003_arm_gic-v2.md#std-dtcompatible-arm-gic-v2"><code>arm,gic-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L38">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>Broadcom BCM2711 VideoCore邮箱（Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L104">已启用：1</a>）</td>
<td><a href="../intercore_reference/P036_BCM2711邮箱绑定.md#dtbinding-brcm-bcm2711-mbox"><code>brcm,bcm2711-mbox</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Broadcom BCM2711引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L114">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P017_brcm_bcm2711-pinctrl.md#std-dtcompatible-brcm-bcm2711-pinctrl"><code>brcm,bcm2711-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">电源域（Power Domain）</td>
<td>板载（On-Board）</td>
<td>Raspberry Pi BCM283x电源域（Power Domain）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L104">已启用：1</a>）</td>
<td><a href="../power_domain_binding_reference/P009_raspberrypi_bcm283x-power.md#std-dtcompatible-raspberrypi-bcm283x-power"><code>raspberrypi,bcm283x-power</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Broadcom iProc RNG200随机数发生器（Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L98">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P006_brcm_iproc-rng200.md#std-dtcompatible-brcm-iproc-rng200"><code>brcm,iproc-rng200</code></a></td>
</tr>
<tr>
<td rowspan="1">传感器（Sensors）</td>
<td>板载（On-Board）</td>
<td>Raspberry Pi BCM283x SoC芯片温度传感器（Die-temperature Sensor）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L88">已启用：1</a>）</td>
<td><a href="../sensor_realtek_rohm_sensirion_binding_reference/P002_raspberrypi_bcm283x-vc-thermal.md#std-dtcompatible-raspberrypi-bcm283x-vc-thermal"><code>raspberrypi,bcm283x-vc-thermal</code></a></td>
</tr>
<tr>
<td rowspan="2">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM PL011通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L146">已禁用：5</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011"><code>arm,pl011</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Broadcom BCM283x辅助UART（Auxiliary UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L156">已启用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P014_brcm_bcm283x-aux-uart.md#std-dtcompatible-brcm-bcm283x-aux-uart"><code>brcm,bcm283x-aux-uart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L83">已启用：2</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L54">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
<tr>
<td rowspan="1">通用串行总线（USB）</td>
<td>片上（On-Chip）</td>
<td>Broadcom BCM2835 USB-OTG，兼容DWC2的控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L272">已启用：1</a>）</td>
<td><a href="../usb_controller_binding_reference/P008_brcm_bcm2835-usb.md#std-dtcompatible-brcm-bcm2835-usb"><code>brcm,bcm2835-usb</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`rpi_4b`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

<a id="tf-card"></a>

### TF存储卡（TF Card）

准备采用MBR分区表及FAT32文件系统的TF卡。在卡的根目录执行以下操作：


1. 下载并放置以下固件文件：


  - [bcm2711-rpi-4-b.dtb](https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/bcm2711-rpi-4-b.dtb)
  - [start4.elf](https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/start4.elf)
  - [fixup4.dat](https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/fixup4.dat)
2. 复制build/zephyr/zephyr.bin。
3. 创建config.txt：

  ```text
  arm_64bit=1
  core_freq=500
  kernel_address=0x200000
  kernel=zephyr.bin
  enable_uart=1
  uart_2ndstage=1
  hdmi_force_hotplug=1
  ```

<a id="console-connection"></a>

### 连接控制台（Console Connection）

将3.3 V USB转UART适配器连接到Raspberry Pi排针：

<table>
<tr>
<th>适配器（Adapter）</th>
<th>Raspberry Pi排针</th>
</tr>
<tr>
<td>地（GND）</td>
<td>第6脚，地（GND）</td>
</tr>
<tr>
<td>接收（Rx）</td>
<td>第8脚，GPIO 14</td>
</tr>
<tr>
<td>发送（Tx）</td>
<td>第10脚，GPIO 15</td>
</tr>
</table>

设置为115200、8N1，无硬件流控制。插入存储卡并给开发板上电，应在GPIO 14／15的串行控制台上看到以下输出：

```text
*** Booting Zephyr OS build v4.4.0-10192-ge201b84b04e4 ***
Secondary CPU core 1 (MPID:0x1) is up
Secondary CPU core 2 (MPID:0x2) is up
Secondary CPU core 3 (MPID:0x3) is up
Hello World! rpi_4b/bcm2711
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://pip.raspberrypi.com/documents/RP-008344-DS-raspberry-pi-4-product-brief.pdf/](https://pip.raspberrypi.com/documents/RP-008344-DS-raspberry-pi-4-product-brief.pdf/)

## 译注

Pi 4B通过MBR／FAT32卡启动，固件、zephyr.bin及config.txt位于卡根目录；3.3 V串口使用排针GPIO14／15。

---

[上一章](P008_Raspberry_Pi_Foundation.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_Raspberry_Pi_5_Cortex-A76.md)
