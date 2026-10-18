---
id: learning.zephyr-docs.boards-rak-raspberry-raytac.page-10
title: Raspberry Pi 5 Cortex-A76
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/raspberrypi/rpi_5/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="rpi_5"></a>

# 第10章\_Raspberry Pi 5（Cortex-A76）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/raspberrypi/rpi_5/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`rpi_5`

厂商（Vendor）：

[Raspberry Pi基金会（Foundation）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=raspberrypi)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[bcm2712](https://docs.zephyrproject.org/latest/boards/index.html#soc=bcm2712)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/raspberrypi/rpi_5/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

[Raspberry Pi 5产品简介（Product Brief）](https://datasheets.raspberrypi.com/rpi5/raspberry-pi-5-product-brief.pdf)

<a id="hardware"></a>

## 硬件（Hardware）


- Broadcom BCM2712，2.4 GHz四核64位Arm Cortex-A76 CPU，带密码运算扩展（Cryptography Extensions）、每核512 KB二级缓存（L2 Cache）及2 MB共享三级缓存（L3 Cache）
- VideoCore VII图形处理器（GPU），支持OpenGL ES 3.1及Vulkan 1.2
- 双路4Kp60 HDMI显示输出，支持高动态范围（HDR）
- 4Kp60 HEVC解码器
- LPDDR4X-4267 SDRAM，可选1、2、4、8及16 GB型号
- 双频802.11ac Wi-Fi
- Bluetooth 5.0及低功耗蓝牙（BLE）
- MicroSD卡槽，支持高速SDR104模式
- 两个USB 3.0端口，支持同时以5 Gbit/s工作
- 两个USB 2.0端口
- 千兆以太网，支持PoE+，需另配PoE+ HAT扩展板
- 两组四通道MIPI摄像头／显示收发器
- PCIe 2.0 x1接口，用于高速外设，需另配M.2 HAT或其他适配器
- 通过USB-C输入5 V／5 A直流电源，支持USB Power Delivery供电协商
- Raspberry Pi标准40引脚排针
- 实时时钟（RTC），由外接电池供电
- 电源按键（Power Button）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`rpi_5`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="rpi_5-hw-features"></a>

<a id="rpi_5-rpi_5/bcm2712-hw-features-section"></a>

#### `rpi_5/bcm2712`目标（Target）

<a id="rpi_5-rpi_5/bcm2712-hw-features-panel"></a>

<a id="rpi_5-rpi_5/bcm2712-hw-features-memory"></a>

该开发板目标的片上存储容量：512 KiB RAM、N/A Flash。

<a id="rpi_5-rpi_5/bcm2712-hw-features-table"></a>

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
<td>Arm Cortex-A76 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L15">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P014_arm_cortex-a76.md#std-dtcompatible-arm-cortex-a76"><code>arm,cortex-a76</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L106">已启用：2</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>BRCMSTB通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P008_brcm_brcmstb-gpio.md#std-dtcompatible-brcm-brcmstb-gpio"><code>brcm,brcmstb-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>RP1外设控制器上的GPIO组（Banks）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L163">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L172">已禁用：2</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P008_raspberrypi_rp1-gpio.md#std-dtcompatible-raspberrypi-rp1-gpio"><code>raspberrypi,rp1-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v2（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P003_arm_gic-v2.md#std-dtcompatible-arm-gic-v2"><code>arm,gic-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_5/rpi_5_bcm2712.dts?plain=1#L31">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>Broadcom BCM2711 VideoCore邮箱（Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L61">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P036_BCM2711邮箱绑定.md#dtbinding-brcm-bcm2711-mbox"><code>brcm,bcm2711-mbox</code></a></td>
</tr>
<tr>
<td rowspan="1">高速外围组件互连（PCIe）</td>
<td>片上（On-Chip）</td>
<td>BRCMSTB PCIe控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L117">已启用：2</a>）</td>
<td><a href="../pcie_memory_virtualization_binding_reference/P005_brcm_brcmstb-pcie.md#std-dtcompatible-brcm-brcmstb-pcie"><code>brcm,brcmstb-pcie</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Broadcom BCM2712引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L98">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P018_brcm_bcm2712-pinctrl.md#std-dtcompatible-brcm-bcm2712-pinctrl"><code>brcm,bcm2712-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Raspberry Pi RP1引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L154">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P001_raspberrypi_rp1-pinctrl.md#std-dtcompatible-raspberrypi-rp1-pinctrl"><code>raspberrypi,rp1-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Broadcom iProc RNG200随机数发生器（Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L55">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P006_brcm_iproc-rng200.md#std-dtcompatible-brcm-iproc-rng200"><code>brcm,iproc-rng200</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM PL011通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L88">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L191">已禁用：5</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011"><code>arm,pl011</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L40">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L24">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="rpi_5-rpi_5/bcm2712/swd-hw-features-section"></a>

#### `rpi_5/bcm2712/swd`目标（Target）

<a id="rpi_5-rpi_5/bcm2712/swd-hw-features-panel"></a>

<a id="rpi_5-rpi_5/bcm2712/swd-hw-features-memory"></a>

该开发板目标的片上存储容量：512 KiB RAM、N/A Flash。

<a id="rpi_5-rpi_5/bcm2712/swd-hw-features-table"></a>

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
<td>Arm Cortex-A76 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L15">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P014_arm_cortex-a76.md#std-dtcompatible-arm-cortex-a76"><code>arm,cortex-a76</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L106">已启用：2</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>BRCMSTB通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../gpio_connectors_bflb_esp_binding_reference/P008_brcm_brcmstb-gpio.md#std-dtcompatible-brcm-brcmstb-gpio"><code>brcm,brcmstb-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>RP1外设控制器上的GPIO组（Banks）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L163">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L172">已禁用：2</a>）</td>
<td><a href="../gpio_raspberrypi_renesas_binding_reference/P008_raspberrypi_rp1-gpio.md#std-dtcompatible-raspberrypi-rp1-gpio"><code>raspberrypi,rp1-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v2（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L46">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P003_arm_gic-v2.md#std-dtcompatible-arm-gic-v2"><code>arm,gic-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_5/rpi_5_bcm2712.dts?plain=1#L31">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">邮箱（Mailbox）</td>
<td>片上（On-Chip）</td>
<td>Broadcom BCM2711 VideoCore邮箱（Mailbox）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L61">已禁用：1</a>）</td>
<td><a href="../intercore_reference/P036_BCM2711邮箱绑定.md#dtbinding-brcm-bcm2711-mbox"><code>brcm,bcm2711-mbox</code></a></td>
</tr>
<tr>
<td rowspan="1">高速外围组件互连（PCIe）</td>
<td>片上（On-Chip）</td>
<td>BRCMSTB PCIe控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L117">已启用：2</a>）</td>
<td><a href="../pcie_memory_virtualization_binding_reference/P005_brcm_brcmstb-pcie.md#std-dtcompatible-brcm-brcmstb-pcie"><code>brcm,brcmstb-pcie</code></a></td>
</tr>
<tr>
<td rowspan="2">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Broadcom BCM2712引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L98">已启用：1</a>）</td>
<td><a href="../pinctrl_adi_ambiq_arm_binding_reference/P018_brcm_bcm2712-pinctrl.md#std-dtcompatible-brcm-bcm2712-pinctrl"><code>brcm,bcm2712-pinctrl</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Raspberry Pi RP1引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L154">已启用：1</a>）</td>
<td><a href="../pinctrl_renesas_silabs_binding_reference/P001_raspberrypi_rp1-pinctrl.md#std-dtcompatible-raspberrypi-rp1-pinctrl"><code>raspberrypi,rp1-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">随机数生成器（RNG）</td>
<td>片上（On-Chip）</td>
<td>Broadcom iProc RNG200随机数发生器（Random Number Generator）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L55">已启用：1</a>）</td>
<td><a href="../rng_binding_reference/P006_brcm_iproc-rng200.md#std-dtcompatible-brcm-iproc-rng200"><code>brcm,iproc-rng200</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM PL011通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L191">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L88">已禁用：5</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011"><code>arm,pl011</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L40">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2712.dtsi?plain=1#L24">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

完整硬件功能列表见[Raspberry Pi硬件资料](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html)。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`rpi_5`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

<a id="blinky"></a>

### 闪灯（Blinky）

步骤概括如下：


1. 将MicroSD卡格式化为MBR分区表及FAT32文件系统。
2. 将以下三个文件保存到卡的根目录。


  - `config.txt`
  - `zephyr.bin`
  - [bcm2712-rpi-5-b.dtb](https://github.com/raspberrypi/firmware/raw/master/boot/bcm2712-rpi-5-b.dtb)
3. 插入MicroSD卡并给Raspberry Pi 5上电。

随后，Raspberry Pi 5将运行zephyr.bin。

<a id="config-txt"></a>

#### `config.txt`

```text
kernel=zephyr.bin
```

<a id="zephyr-bin"></a>

#### `zephyr.bin`

构建应用，例如[Blinky](../getting_started/P004_LED闪烁示例.md#blinky)。

```text
# From the root of the zephyr repository
west build -b rpi_5 samples/basic/blinky
```

将build/zephyr目录中的zephyr.bin复制到MicroSD卡根目录。

插入MicroSD卡并给Raspberry Pi 5上电，STAT LED随后开始闪烁。

<a id="serial-communication"></a>

### 串行通信（Serial Communication）

<a id="wiring"></a>

#### 接线（Wiring）

需要准备以下物品：


- [Raspberry Pi调试探针（Debug Probe）](https://www.raspberrypi.com/products/debug-probe/)
- JST线缆：两端均为3针JST连接器
- USB线缆：USB-A公头到Micro-USB-B公头

使用JST线缆，将Raspberry Pi Debug Probe的UART端口连接到Raspberry Pi 5两个HDMI接口之间的UART端口。

随后用USB线缆将Raspberry Pi Debug Probe连接到电脑。

<a id="id1"></a>

#### `config.txt`

```text
kernel=zephyr.bin
enable_uart=1
uart_2ndstage=1
```

<a id="id2"></a>

#### `zephyr.bin`

构建应用，例如[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)：

```text
# From the root of the zephyr repository
west build -b rpi_5 samples/hello_world
```

将build/zephyr目录中的zephyr.bin复制到MicroSD卡根目录。

将MicroSD卡插入Raspberry Pi 5。

<a id="serial-terminal-emulator"></a>

#### 串口终端模拟器（Serial Terminal Emulator）

给Raspberry Pi 5上电后，将在串行控制台中看到以下输出：

```text
*** Booting Zephyr OS build XXXXXXXXXXXX  ***
Hello World! rpi_5/bcm2712
```

<a id="xen-dom0"></a>

### Xen控制域（Dom0）

Raspberry Pi 5可作为Xen Zephyr Dom0运行，此时可使用xen-dom0配置片段（Snippet）。

以下命令演示将Raspberry Pi 5上的Zephyr构建为Dom0：

```text
west build -b rpi_5 -p always -S xen-dom0 samples/hello_world
```

此配置预期与负责Xen Domain-0／Dom0功能的专用应用配合。

注意（Note）

需要在应用设备树覆盖文件（Devicetree Overlay）中指定hypervisor@x及memory@x节点，取值应采用Xen启动时提供的值。通常Xen会更新目标内核的设备树，但Zephyr不支持这种更新方式。详情见“[Xen Dom0：Xen控制域通用配置片段](../snippets/P022_Xen控制域配置片段.md#xen-dom0)”。

## 译注

Pi 5需在卡根目录放置config.txt、zephyr.bin及bcm2712-rpi-5-b.dtb；串口位于两个HDMI口之间的3针接口。Xen Dom0需专用应用及启动信息对应的设备树节点。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [raspberry-pi.html](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html)：HTTP Error 403: Forbidden。
- [](https://www.raspberrypi.com/products/debug-probe/)：HTTP Error 403: Forbidden。

---

[上一章](P009_Raspberry_Pi_4_Model_B_Cortex-A72.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_Raspberry_Pi_Debug_Probe.md)
