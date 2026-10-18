---
id: learning.zephyr-docs.boards-fanke-to-gardena.page-7
title: ROC-RK3568-PC Quad-core Cortex-A55
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/firefly/roc_rk3568_pc/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="roc_rk3568_pc"></a>

# 第7章\_ROC-RK3568-PC（四核Cortex-A55）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/firefly/roc_rk3568_pc/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`roc_rk3568_pc`

厂商（Vendor）：

[Firefly](https://docs.zephyrproject.org/latest/boards/index.html#vendor=firefly)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[rk3568](https://docs.zephyrproject.org/latest/boards/index.html#soc=rk3568)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/firefly/roc_rk3568_pc/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

ROC-RK3568-PC是一台四核64位微型计算机，支持4G大内存。M.2和SATA 3.0接口支持扩展大容量硬盘。它提供两个千兆以太网端口，支持Wi-Fi 6无线传输，控制端口可连接RS485／RS232设备。

RK3568是采用Armv8.2-A架构的四核64位Cortex-A55处理器，最高频率2.0 GHz。Zephyr OS已移植到该处理器运行。


- 开发板特性（Board Features）：


  - 内存（RAM）：4 GB LPDDR4
  - 存储（Storage）：


    - 32 GB嵌入式多媒体卡（eMMC）
    - M.2 PCIe 3.0 × 1，可扩展2242／2280规格NVMe固态硬盘（SSD）
    - TF卡槽（TF-Card Slot）
  - 无线（Wireless）：


    - 支持Wi-Fi 6（802.11ax）
    - 支持蓝牙5.0（BT 5.0）
  - USB:


    - 1路USB 3.0
    - 2路USB 2.0
    - 1个Type-C接口
  - 以太网（Ethernet）
  - M.2 PCIe 3.0，可扩展NVMe SSD
  - 发光二极管（LED）：


    - 1个电源状态LED
  - 调试（Debug）


    - 开发板UART调试端口

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`roc_rk3568_pc`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="roc_rk3568_pc-hw-features"></a>

<a id="roc_rk3568_pc-roc_rk3568_pc/rk3568-hw-features-section"></a>

#### `roc_rk3568_pc/rk3568`目标（Target）

<a id="roc_rk3568_pc-roc_rk3568_pc/rk3568-hw-features-panel"></a>

<a id="roc_rk3568_pc-roc_rk3568_pc/rk3568-hw-features-memory"></a>

该开发板目标的片上存储容量：1 MiB RAM、N/A Flash。

<a id="roc_rk3568_pc-roc_rk3568_pc/rk3568-hw-features-table"></a>

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
<td>Arm Cortex-A55 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3568.dtsi?plain=1#L26">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P009_arm_cortex-a55.md#std-dtcompatible-arm-cortex-a55"><code>arm,cortex-a55</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3568.dtsi?plain=1#L55">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>片上（On-Chip）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3568.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3568.dtsi?plain=1#L80">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/firefly/roc_rk3568_pc/roc_rk3568_pc.dts?plain=1#L22">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3568.dtsi?plain=1#L71">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="roc_rk3568_pc-roc_rk3568_pc/rk3568/smp-hw-features-section"></a>

#### `roc_rk3568_pc/rk3568/smp`目标（Target）

<a id="roc_rk3568_pc-roc_rk3568_pc/rk3568/smp-hw-features-panel"></a>

<a id="roc_rk3568_pc-roc_rk3568_pc/rk3568/smp-hw-features-memory"></a>

该开发板目标的片上存储容量：1 MiB RAM、N/A Flash。

<a id="roc_rk3568_pc-roc_rk3568_pc/rk3568/smp-hw-features-table"></a>

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
<td>Arm Cortex-A55 CPU（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3568.dtsi?plain=1#L26">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P009_arm_cortex-a55.md#std-dtcompatible-arm-cortex-a55"><code>arm,cortex-a55</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3568.dtsi?plain=1#L55">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>片上（On-Chip）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3568.dtsi?plain=1#L66">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>ns16550通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3568.dtsi?plain=1#L80">已启用：1</a>）</td>
<td><a href="../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550"><code>ns16550</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/firefly/roc_rk3568_pc/roc_rk3568_pc.dts?plain=1#L22">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/rockchip/rk3568.dtsi?plain=1#L71">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="devices"></a>

### 设备（Devices）

<a id="system-clock"></a>

#### 系统时钟（System Clock）

此开发板配置使用24 MHz系统时钟，Cortex-A55内核最高运行于2.0 GHz。

<a id="serial-port"></a>

#### 串口（Serial Port）

此配置通过CPU的UART2使用一个串行通信通道。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`roc_rk3568_pc`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

使用U-Boot将`zephyr.bin`加载到内存并启动：

```text
tftp 0x40000000 zephyr.bin; dcache flush; icache flush; dcache off; icache off; go 0x40000000
```

此配置可运行基础Zephyr应用及内核测试，例如[基础同步（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)示例：

```text
# From the root of the zephyr repository
west build -b roc_rk3568_pc samples/synchronization
west build -t run
```

这会构建包含同步示例应用的镜像，启动它并显示以下RAM控制台输出：

```text
***  Booting Zephyr OS build bc695c6df5eb  ***
thread_a: Hello World from cpu 0 on roc_rk3568_pc!
thread_b: Hello World from cpu 0 on roc_rk3568_pc!
thread_a: Hello World from cpu 0 on roc_rk3568_pc!
thread_b: Hello World from cpu 0 on roc_rk3568_pc!
```

对于`roc_rk3568_pc//smp`支持，可使用此配置运行Zephyr对称多处理（SMP）应用及子系统测试，例如基础同步示例：（[基础同步（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)）

```text
# From the root of the zephyr repository
west build -b roc_rk3568_pc//smp samples/synchronization
west build -t run
```

这会构建包含`shell_module`示例应用的镜像，启动它并显示以下RAM控制台输出：

```text
***  Booting Zephyr OS build bc695c6df5eb  ***
I/TC: Secondary CPU 1 initializing
I/TC: Secondary CPU 1 switching to normal world boot
I/TC: Secondary CPU 2 initializing
I/TC: Secondary CPU 2 switching to normal world boot
I/TC: Secondary CPU 3 initializing
I/TC: Secondary CPU 3 switching to normal world boot
Secondary CPU core 1 (MPID:0x100) is up
Secondary CPU core 2 (MPID:0x200) is up
Secondary CPU core 3 (MPID:0x300) is up

thread_a: Hello World from cpu 0 on roc_rk3568_pc!
thread_b: Hello World from cpu 1 on roc_rk3568_pc!
thread_a: Hello World from cpu 0 on roc_rk3568_pc!
thread_b: Hello World from cpu 1 on roc_rk3568_pc!
```

<a id="references"></a>

### 参考资料（References）

更多信息见Firefly官方网站（Firefly Website）。（[Firefly网站](https://en.t-firefly.com/product/industry/rocrk3568pc.html?theme=pc)）

## 译注

原文用基础同步示例展示构建，却在部分运行说明中称shell_module；原标题、命令与示例输出分别保留。目标表中的1 MiB RAM是该Zephyr目标的配置容量，不能与开发板物理4 GB内存混为一项。

---

[上一章](P006_Firefly.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P008_ROC-RK3588-PC_Quad-core_Cortex-A55.md)
