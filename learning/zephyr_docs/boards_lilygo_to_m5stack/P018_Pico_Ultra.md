---
id: learning.zephyr-docs.boards-lilygo-to-m5stack.page-18
title: Pico Ultra
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/luckfox/pico_ultra/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="pico_ultra"></a>

# 第18章\_Pico Ultra

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/luckfox/pico_ultra/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/pico_ultra.webp](images/pico_ultra.webp)](images/pico_ultra.webp)

Pico Ultra

名称（Name）：

`pico_ultra`

厂商（Vendor）：

[深圳Luckfox科技有限公司（Shenzhen Luckfox Technology Co., Ltd.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=luckfox)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[rv1106](https://docs.zephyrproject.org/latest/boards/index.html#soc=rv1106)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/luckfox/pico_ultra/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

[Luckfox Pico Ultra W](https://wiki.luckfox.com/Luckfox-Pico-Ultra)是基于Rockchip RV1106芯片的低成本微型Linux开发板，配备256 MB DDR3L DRAM。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`pico_ultra`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="pico_ultra-hw-features"></a>

<a id="pico_ultra-pico_ultra/rv1106-hw-features-section"></a>

#### `pico_ultra/rv1106`目标（Target）

<a id="pico_ultra-pico_ultra/rv1106-hw-features-panel"></a>

<a id="pico_ultra-pico_ultra/rv1106-hw-features-memory"></a>

该开发板目标的片上存储容量：256 MiB RAM、N/A Flash。

<a id="pico_ultra-pico_ultra/rv1106-hw-features-table"></a>

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
<td>Arm Cortex-A7 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/rockchip/rv1106.dtsi?plain=1#L22">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P011_arm_cortex-a7.md#std-dtcompatible-arm-cortex-a7"><code>arm,cortex-a7</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v2（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/rockchip/rv1106.dtsi?plain=1#L45">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P003_arm_gic-v2.md#std-dtcompatible-arm-gic-v2"><code>arm,gic-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/rockchip/rv1106.dtsi?plain=1#L73">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/rockchip/rv1106.dtsi?plain=1#L55">已禁用：5</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/luckfox/pico_ultra/pico_ultra.dts?plain=1#L21">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/rockchip/rv1106.dtsi?plain=1#L29">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

运行Zephyr之前，必须通过Luckfox SDK的U-Boot初始化Rockchip RV1106。

<a id="modifying-u-boot"></a>

### 修改U-Boot（Modifying U-Boot）

必须修改默认U-Boot，启用缓存命令，并阻止强制进入Thumb模式。将以下补丁应用到Luckfox SDK：

```text
--- a/sysdrv/source/uboot/u-boot/cmd/boot.c
+++ b/sysdrv/source/uboot/u-boot/cmd/boot.c
@@ -21,10 +21,6 @@
 unsigned long do_go_exec(ulong (*entry)(int, char * const []), int argc,
                                  char * const argv[])
 {
-#ifdef CONFIG_CPU_V7
-    ulong addr = (ulong)entry | 1;
-    entry = (void *)addr;
-#endif
     return entry (argc, argv);
 }

--- a/sysdrv/source/uboot/u-boot/configs/luckfox_rv1106_uboot_defconfig
+++ b/sysdrv/source/uboot/u-boot/configs/luckfox_rv1106_uboot_defconfig
@@ -141,3 +141,4 @@
 CONFIG_SPL_GZIP=y
 CONFIG_ERRNO_STR=y
 # CONFIG_EFI_LOADER is not set
+CONFIG_CMD_CACHE=y
```

按官方[Luckfox Pico SDK](https://github.com/LuckfoxTECH/luckfox-pico)说明重新构建并烧录U-Boot。

<a id="building-and-running"></a>

### 构建与运行（Building and Running）

构建Zephyr应用：

```text
# From the root of the zephyr repository
west build -b pico_ultra samples/hello_world
```

通过TFTP加载二进制文件，禁用并刷新缓存（Caches），然后启动Zephyr：

```text
=> dcache off && icache off
=> dcache flush && icache flush
=> setenv ipaddr 192.168.1.2
=> setenv serverip 192.168.1.1
=> tftp 0x0 zephyr.bin
=> go 0x0
```

串行控制台应显示以下输出：

```text
*** Booting Zephyr OS build v4.3.0-4280-g2f3d729d951a ***
Hello World! pico_ultra/rv1106
```

## 译注

Zephyr启动前必须先由Luckfox SDK U-Boot初始化硬件；缓存命令及防止强制Thumb模式的补丁属于原文前置步骤。

---

[上一章](P017_Shenzhen_Luckfox_Technology_Co._Ltd..md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P019_M5Stack.md)
