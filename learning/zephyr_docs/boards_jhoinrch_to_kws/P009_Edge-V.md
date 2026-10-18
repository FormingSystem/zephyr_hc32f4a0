---
id: learning.zephyr-docs.boards-jhoinrch-to-kws.page-9
title: Edge-V
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/khadas/edgev/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="khadas_edgev"></a>

# 第9章\_Edge-V

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/khadas/edgev/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`khadas_edgev`

厂商（Vendor）：

[Khadas](https://docs.zephyrproject.org/latest/boards/index.html#vendor=khadas)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[rk3399](https://docs.zephyrproject.org/latest/boards/index.html#soc=rk3399)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/khadas/edgev/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

参见<[https://www.khadas.com/edge-v](https://www.khadas.com/edge-v)>。

<a id="hardware"></a>

## 硬件（Hardware）

参见<[https://docs.khadas.com/products/sbc/edge1/hardware/start](https://docs.khadas.com/products/sbc/edge1/hardware/start)>。

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`khadas_edgev`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="khadas_edgev-hw-features"></a>

<a id="khadas_edgev-khadas_edgev/rk3399-hw-features-section"></a>

#### `khadas_edgev/rk3399`目标（Target）

<a id="khadas_edgev-khadas_edgev/rk3399-hw-features-panel"></a>

<a id="khadas_edgev-khadas_edgev/rk3399-hw-features-memory"></a>

该开发板目标的片上存储容量：128 MiB RAM、N/A Flash。

<a id="khadas_edgev-khadas_edgev/rk3399-hw-features-table"></a>

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
<td>ARM Cortex-A53处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3399.dtsi?plain=1#L19">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P008_arm_cortex-a53.md#std-dtcompatible-arm-cortex-a53"><code>arm,cortex-a53</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3399.dtsi?plain=1#L56">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3399.dtsi?plain=1#L91">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3399.dtsi?plain=1#L78">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

开发板具有多个串口，Zephyr使用uart2作为串行控制台。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`khadas_edgev`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

使用以下配置，在Khadas Edge-V上运行基础Zephyr应用及内核测试。以[Hello World](../getting_started/P005_HelloWorld示例.md#hello_world)为例：


1. 非SMP模式，即不启用对称多处理（Non-SMP）

```text
# From the root of the zephyr repository
west build -b khadas_edgev samples/hello_world
```

这会构建包含同步（Synchronization）示例应用的镜像。

构建Zephyr镜像：

```text
mkimage -C none -A arm64 -O linux -a 0x10000000 -e 0x10000000 -d build/zephyr/zephyr.bin build/zephyr/zephyr.img
```

使用U-Boot加载Zephyr.bin，并在CPU内核0上启动：

```text
tftpboot ${pxefile_addr_r} zephyr.img; bootm start ${pxefile_addr_r}; bootm loados; bootm go
```

控制台应显示以下输出：

```text
*** Booting Zephyr OS build XXXXXXXXXXXX  ***
Hello World! khadas_edgev
```

<a id="flashing"></a>

### 烧录（Flashing）

可在U-Boot中从SD卡、eMMC、QSPI闪存或网络，将Zephyr镜像加载到DDR内存地址0x10000000。

<a id="references"></a>

### 参考资料（References）

[文档（Documentation）：](https://docs.khadas.com/products/sbc/edge1/start)

## 译注

原文以Hello World引入，随后又写同步示例；两种名称按各段来源保留。

---

[上一章](P008_Edge2.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_Khadas.md)
