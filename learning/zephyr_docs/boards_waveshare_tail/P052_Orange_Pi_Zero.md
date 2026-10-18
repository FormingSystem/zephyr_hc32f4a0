---
id: learning.zephyr-docs.boards-waveshare-tail.page-52
title: Orange Pi Zero
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/xunlong/opi_zero/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="opi_zero"></a>

# 第52章\_Orange Pi Zero

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/xunlong/opi_zero/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/opi_zero.webp](images/opi_zero.webp)](images/opi_zero.webp)

Orange Pi Zero

名称（Name）：

`opi_zero`

厂商（Vendor）：

[深圳迅龙软件有限公司（Shenzhen Xunlong Software CO.,Limited）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=xunlong)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[sun8i_h3](https://docs.zephyrproject.org/latest/boards/index.html#soc=sun8i_h3)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/xunlong/opi_zero/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

[Orange Pi Zero](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-Zero.html)是开源单板计算机，采用全志（Allwinner）H2+／H3 SoC，配备256 MB或512 MB DDR3 SDRAM；SoC采用四核ARM Cortex-A7。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`opi_zero`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="opi_zero-hw-features"></a>

<a id="opi_zero-opi_zero/sun8i_h3-hw-features-section"></a>

#### `opi_zero/sun8i_h3`目标（Target）

<a id="opi_zero-opi_zero/sun8i_h3-hw-features-panel"></a>

<a id="opi_zero-opi_zero/sun8i_h3-hw-features-memory"></a>

该开发板目标的片上存储容量：512 MiB RAM、N/A Flash。

<a id="opi_zero-opi_zero/sun8i_h3-hw-features-table"></a>

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
<td>Arm Cortex-A7 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/allwinner/sun8i-h3.dtsi?plain=1#L22">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P011_arm_cortex-a7.md#std-dtcompatible-arm-cortex-a7"><code>arm,cortex-a7</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v2（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/allwinner/sun8i-h3.dtsi?plain=1#L62">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P003_arm_gic-v2.md#std-dtcompatible-arm-gic-v2"><code>arm,gic-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/allwinner/sun8i-h3.dtsi?plain=1#L72">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/allwinner/sun8i-h3.dtsi?plain=1#L82">已禁用：3</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/xunlong/opi_zero/opi_zero.dts?plain=1#L21">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/allwinner/sun8i-h3.dtsi?plain=1#L47">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`opi_zero`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

运行Zephyr前须初始化Allwinner H2+／H3，可采用Das U-Boot二级程序加载器（Secondary Program Loader，SPL）等方式。

本节使用U-Boot SPL。U-Boot与Allwinner H2+／H3配合使用的详细说明见：


- [Das U-Boot网站](https://docs.u-boot.org/en/latest/)
- [在Allwinner SoC上使用U-Boot](https://docs.u-boot.org/en/stable/board/allwinner/sunxi.html)

<a id="building-das-u-boot"></a>

### 构建Das U-Boot（Building Das U-Boot）

为Orange Pi Zero克隆并构建Das U-Boot：

```text
git clone -b v2024.01 https://source.denx.de/u-boot/u-boot.git
cd u-boot
make distclean
make orangepi_zero_defconfig
export PATH=/path/to/zephyr-sdk/arm-zephyr-eabi/bin/:$PATH
export CROSS_COMPILE=arm-zephyr-eabi-
make
sudo dd if=u-boot-sunxi-with-spl.bin of=/dev/mmcblkX bs=1024 seek=8
```

<a id="building-and-flashing"></a>

### 构建与烧录（Building and Flashing）

```text
# From the root of the zephyr repository
west build -b opi_zero samples/hello_world
```

将编译好的zephyr.bin复制到SD卡boot目录，再将卡插入板卡。

```text
=> fatload mmc 0:1 0x40000000 /boot/zephyr.bin
=> go 0x40000000
```

串行控制台应显示以下输出：

```text
*** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx ***
Hello World! opi_zero/sun8i_h3
```

## 译注

Orange Pi Zero运行Zephyr前需由U-Boot SPL等初始化H2+／H3。

---

[上一章](P051_Shenzhen_Xunlong_Software_Co._Limited.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P053_Orange_Pi_Zero_2W.md)
