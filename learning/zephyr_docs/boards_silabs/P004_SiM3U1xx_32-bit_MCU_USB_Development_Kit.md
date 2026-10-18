---
id: learning.zephyr-docs.boards-silabs.page-4
title: SiM3U1xx 32-bit MCU USB Development Kit
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/silabs/dev_kits/sim3u1xx_dk/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="sim3u1xx_dk"></a>

# 第4章\_SiM3U1xx 32位MCU USB开发套件

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/silabs/dev_kits/sim3u1xx_dk/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../../_images/sim3u1xx_dk.webp](images/sim3u1xx_dk.webp)](images/sim3u1xx_dk.webp)

SiM3U1xx 32位MCU USB开发套件

名称（Name）：

`sim3u1xx_dk`

厂商（Vendor）：

[芯科科技（Silicon Laboratories）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=silabs)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[sim3u167](https://docs.zephyrproject.org/latest/boards/index.html#soc=sim3u167)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/dev_kits/sim3u1xx_dk/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

<a id="id12"></a>

此开发套件[注3](#id6)用于为SiM3U1xx MCU开发软件。（[开发套件（development kit）](https://www.silabs.com/development-tools/mcu/32-bit/sim3u1xx-development-kit)）

<a id="hardware"></a>

## 硬件（Hardware）


- Silicon Labs SiM3U167-B-GM片上系统（SoC）
- CPU内核：Arm Cortex-M3
- 闪存容量：256 kB
- RAM容量：32 kB
- 输入输出（IO）：


  - 2个用户LED
  - 2个用户按键
  - 2个电源LED
  - 复位按键
  - 电位器（Potentiometer）
  - 模拟端子
  - 电容检测滑条及按键
  - USB虚拟COM端口

SiM3U167 SoC及SiM3U1xx开发板更多信息见：


- <a id="id3"></a>

  Silicon Labs [SiM3U1xx](https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx)[注1](#id2)
- <a id="id5"></a>

  Silicon Labs [SiM3U167-B-GM](https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx/device.sim3u167-b-gm)[注2](#id4)
- <a id="id7"></a>

  Silicon Labs [SiM3U1xx-B-DK](https://www.silabs.com/development-tools/mcu/32-bit/sim3u1xx-development-kit)[注3](#id6)
- <a id="id9"></a>

  Silicon Labs SiM3U1xx-B-DK MCU卡用户指南[注4](#id8)（[用户指南（user’s guide）](https://www.silabs.com/documents/public/user-guides/UPMU-M3U160.pdf)）
- <a id="id11"></a>

  Silicon Labs SiM3U1xx及SiM3C1xx B版勘误（[Errata](https://www.silabs.com/documents/public/errata/SiM3U1xx-SiM3C1xxErrata.pdf)）[注5](#id10)

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`sim3u1xx_dk`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="sim3u1xx_dk-hw-features"></a>

<a id="sim3u1xx_dk-sim3u1xx_dk/sim3u167-hw-features-section"></a>

#### `sim3u1xx_dk/sim3u167`目标（Target）

<a id="sim3u1xx_dk-sim3u1xx_dk/sim3u167-hw-features-panel"></a>

<a id="sim3u1xx_dk-sim3u1xx_dk/sim3u167-hw-features-memory"></a>

该开发板目标的片上存储容量：32 KiB RAM、256 KiB Flash。

<a id="sim3u1xx_dk-sim3u1xx_dk/sim3u167-hw-features-table"></a>

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
<td>ARM Cortex-M3处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L20">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P021_arm_cortex-m3.md#std-dtcompatible-arm-cortex-m3"><code>arm,cortex-m3</code></a></td>
</tr>
<tr>
<td rowspan="3">时钟控制（Clock Control）</td>
<td>片上（On-Chip）</td>
<td>Silabs Si32 PLL时钟控制器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L41">已启用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P010_silabs_si32-pll.md#std-dtcompatible-silabs-si32-pll"><code>silabs,si32-pll</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silabs Si32 AHB时钟控制器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L48">已启用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P008_silabs_si32-ahb.md#std-dtcompatible-silabs-si32-ahb"><code>silabs,si32-ahb</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Silabs Si32 APB时钟控制器节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L54">已启用：1</a>）</td>
<td><a href="../clock_silabs_ti_xilinx_binding_reference/P009_silabs_si32-apb.md#std-dtcompatible-silabs-si32-apb"><code>silabs,si32-apb</code></a></td>
</tr>
<tr>
<td rowspan="1">密码学加速器（Cryptographic Accelerator）</td>
<td>片上（On-Chip）</td>
<td>Si32高级加密标准（AES）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L76">已启用：1</a>）</td>
<td><a href="../crypto_secure_engine_st_ti_binding_reference/P014_silabs_si32-aes.md#std-dtcompatible-silabs-si32-aes"><code>silabs,si32-aes</code></a></td>
</tr>
<tr>
<td rowspan="1">直接存储器访问（DMA）</td>
<td>片上（On-Chip）</td>
<td>Si32直接存储器访问（DMA）控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L64">已启用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_dma_binding_reference/P002_silabs_si32-dma.md#std-dtcompatible-silabs-si32-dma"><code>silabs,si32-dma</code></a></td>
</tr>
<tr>
<td rowspan="1">闪存控制器（Flash Controller）</td>
<td>片上（On-Chip）</td>
<td>Silabs Si32闪存控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L87">已启用：1</a>）</td>
<td><a href="../flash_renesas_st_ti_binding_reference/P009_silabs_si32-flash-controller.md#std-dtcompatible-silabs-si32-flash-controller"><code>silabs,si32-flash-controller</code></a></td>
</tr>
<tr>
<td rowspan="1">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Si32通用输入输出（GPIO）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L119">已启用：4</a>）</td>
<td><a href="../gpio_silabs_st_connectors_binding_reference/P016_silabs_si32-gpio.md#std-dtcompatible-silabs-si32-gpio"><code>silabs,si32-gpio</code></a></td>
</tr>
<tr>
<td rowspan="1">输入（Input）</td>
<td>板载（On-Board）</td>
<td>一组绑定到 GPIO 的输入按键（GPIO-Bound Input Keys）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sim3u1xx_dk/sim3u1xx_dk.dts?plain=1#L45">已启用：1</a>）</td>
<td><a href="../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys"><code>gpio-keys</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P002_ARMv7_M_NVIC.md#std-dtcompatible-arm-v7m-nvic"><code>arm,v7m-nvic</code></a></td>
</tr>
<tr>
<td rowspan="1">发光二极管（LED）</td>
<td>板载（On-Board）</td>
<td>一组由 GPIO 控制的 LED（GPIO-Controlled LEDs）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/sim3u1xx_dk/sim3u1xx_dk.dts?plain=1#L31">已启用：1</a>）</td>
<td><a href="../hardware/P564_GPIO指示灯绑定.md#dtbinding-gpio-leds"><code>gpio-leds</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L95">已启用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Silabs Si32引脚控制器（Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L32">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P001_silabs_si32-pinctrl.md#std-dtcompatible-silabs-si32-pinctrl"><code>silabs,si32-pinctrl</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Si32通用同步异步收发器（USART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L103">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L111">已禁用：1</a>）</td>
<td><a href="../uart_silabs_stm32_ti_binding_reference/P009_silabs_si32-usart.md#std-dtcompatible-silabs-si32-usart"><code>silabs,si32-usart</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>片上（On-Chip）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/silabs/sim3u.dtsi?plain=1#L28">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>ARMv7-M 系统节拍（System Tick）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P006_ARMv7_M_SysTick.md#std-dtcompatible-arm-armv7m-systick"><code>arm,armv7m-systick</code></a></td>
</tr>
</table>

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

<table>
<tr>
<th>引脚（Pin）</th>
<th>名称（Name）</th>
<th>注意（Note）</th>
</tr>
<tr>
<td>PB1.12</td>
<td>发送（TX），输出（O）</td>
<td rowspan="4">通过USB虚拟COM端口与主机建立串口连接</td>
</tr>
<tr>
<td>PB1.13</td>
<td>接收（RX），输入（I）</td>
</tr>
<tr>
<td>PB1.14</td>
<td>请求发送（RTS），输出（O）</td>
</tr>
<tr>
<td>PB1.15</td>
<td>允许发送（CTS），输入（I）</td>
</tr>
<tr>
<td>PB2.8</td>
<td>按键开关SW2</td>
<td></td>
</tr>
<tr>
<td>PB2.9</td>
<td>按键开关SW3</td>
<td></td>
</tr>
<tr>
<td>PB2.10</td>
<td>红色LED，DS3</td>
<td></td>
</tr>
<tr>
<td>PB2.11</td>
<td>黄色LED，DS4</td>
<td></td>
</tr>
<tr>
<td>PB1.5</td>
<td>电位器（Potentiometer）</td>
<td></td>
</tr>
<tr>
<td>PB2.12</td>
<td>电位器偏置（Potentiometer Bias）</td>
<td></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`sim3u1xx_dk`开发板支持下表所列的运行工具（Runners）及相关west命令。

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
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-openocd">openocd</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
<td>✅</td>
<td></td>
<td>✅</td>
</tr>
</table>

<a id="flashing"></a>

### 烧录（Flashing）

下面以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例，构建Zephyr内核及应用：

```text
# From the root of the zephyr repository
west build -b sim3u1xx_dk samples/hello_world
```

使用两个USB端口将sim3u1xx_dk连接主机，应能看到USB串口连接。

打开串口终端（如minicom或PuTTY），设置如下：


- 速率（Speed）：115200波特率
- 数据位（Data）：8位
- 奇偶校验（Parity）：无（None）
- 停止位（Stop Bits）：1位

复位开发板后，对应串口终端应显示以下消息：

```text
Hello World! sim3u1xx_dk/sim3u167
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx](https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx/device.sim3u167-b-gm](https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx/device.sim3u167-b-gm)

<a id="id6"></a>

〔3〕 ([1](#id7),[2](#id12)) [https://www.silabs.com/development-tools/mcu/32-bit/sim3u1xx-development-kit](https://www.silabs.com/development-tools/mcu/32-bit/sim3u1xx-development-kit)

<a id="id8"></a>

〔[4](#id9)〕 [https://www.silabs.com/documents/public/user-guides/UPMU-M3U160.pdf](https://www.silabs.com/documents/public/user-guides/UPMU-M3U160.pdf)

<a id="id10"></a>

〔[5](#id11)〕 [https://www.silabs.com/documents/public/errata/SiM3U1xx-SiM3C1xxErrata.pdf](https://www.silabs.com/documents/public/errata/SiM3U1xx-SiM3C1xxErrata.pdf)

## 译注

SiM3U1xx-DK需要连接调试适配器及开发板的两条USB线，按原文供电和连接步骤操作。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [sim3u1xx-development-kit](https://www.silabs.com/development-tools/mcu/32-bit/sim3u1xx-development-kit)：HTTP Error 403: Forbidden。
- [SiM3U1xx-SiM3C1xxErrata.pdf](https://www.silabs.com/documents/public/errata/SiM3U1xx-SiM3C1xxErrata.pdf)：HTTP Error 403: Forbidden。
- [UPMU-M3U160.pdf](https://www.silabs.com/documents/public/user-guides/UPMU-M3U160.pdf)：HTTP Error 403: Forbidden。
- [precision32-sim3u1xx](https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx)：HTTP Error 403: Forbidden。
- [device.sim3u167-b-gm](https://www.silabs.com/mcu/32-bit-microcontrollers/precision32-sim3u1xx/device.sim3u167-b-gm)：HTTP Error 403: Forbidden。

---

[上一章](P003_EFM32PG28_Pro_Kit_PG28-PK2506A.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_SiWx917_Wi-Fi_6_and_Bluetooth_LE_SoC_Dev_Kit_BRD2605A.md)
