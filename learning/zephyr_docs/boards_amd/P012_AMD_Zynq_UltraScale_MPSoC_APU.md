---
id: learning.zephyr-docs.boards-amd.page-12
title: AMD Zynq UltraScale MPSoC APU
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/amd/zynqmp_apu/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="zynqmp_apu"></a>

# 第12章\_AMD Zynq UltraScale+多处理器片上系统应用处理单元（MPSoC APU）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/amd/zynqmp_apu/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`zynqmp_apu`

厂商（Vendor）：

[Advanced Micro Devices（AMD）, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=amd)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[`zynqmp_apu`](https://docs.zephyrproject.org/latest/boards/index.html#soc=zynqmp_apu)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/amd/zynqmp_apu/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

此开发板面向AMD Zynq UltraScale+ MPSoC器件上的Cortex-A53应用处理单元（APU）。APU集群的GIC-400地址为`0xf9010000`，高地址DDR为`0x8_0000_0000`，处理系统UART0（PS UART0）为`0xff000000`。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`zynqmp_apu`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="zynqmp_apu-hw-features"></a>

<a id="zynqmp_apu-zynqmp_apu/zynqmp_apu-hw-features-section"></a>

#### `zynqmp_apu/zynqmp_apu`目标（Target）

<a id="zynqmp_apu-zynqmp_apu/zynqmp_apu-hw-features-panel"></a>

<a id="zynqmp_apu-zynqmp_apu/zynqmp_apu-hw-features-memory"></a>

该开发板目标的片上存储容量：2 GiB RAM、N/A Flash。

<a id="zynqmp_apu-zynqmp_apu/zynqmp_apu-hw-features-table"></a>

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
<td>ARM Cortex-A53处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/zynqmp_a53.dtsi?plain=1#L21">已启用：1</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P008_arm_cortex-a53.md#std-dtcompatible-arm-cortex-a53"><code>arm,cortex-a53</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v2（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/zynqmp_a53.dtsi?plain=1#L48">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P003_arm_gic-v2.md#std-dtcompatible-arm-gic-v2"><code>arm,gic-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>片上（On-Chip）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/zynqmp_a53.dtsi?plain=1#L29">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Xilinx处理系统通用异步收发器（PS UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/zynqmp_a53.dtsi?plain=1#L57">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/zynqmp_a53.dtsi?plain=1#L65">已禁用：1</a>）</td>
<td><a href="../uart_ti_wch_virtual_binding_reference/P011_xlnx_xuartps.md#std-dtcompatible-xlnx-xuartps"><code>xlnx,xuartps</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/amd/zynqmp_apu/zynqmp_apu.dts?plain=1#L22">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>Xilinx处理系统三通道定时计数器（PS Triple-Timer Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/zynqmp_a53.dtsi?plain=1#L73">已禁用：4</a>）</td>
<td><a href="../mcu_timer_binding_reference/P014_xlnx_ttcps.md#std-dtcompatible-xlnx-ttcps"><code>xlnx,ttcps</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/zynqmp_a53.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="zynqmp_apu-zynqmp_apu/zynqmp_apu/smp-hw-features-section"></a>

#### `zynqmp_apu/zynqmp_apu/smp`目标（Target）

<a id="zynqmp_apu-zynqmp_apu/zynqmp_apu/smp-hw-features-panel"></a>

<a id="zynqmp_apu-zynqmp_apu/zynqmp_apu/smp-hw-features-memory"></a>

该开发板目标的片上存储容量：2 GiB RAM、N/A Flash。

<a id="zynqmp_apu-zynqmp_apu/zynqmp_apu/smp-hw-features-table"></a>

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
<td>ARM Cortex-A53处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/zynqmp_a53.dtsi?plain=1#L21">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P008_arm_cortex-a53.md#std-dtcompatible-arm-cortex-a53"><code>arm,cortex-a53</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v2（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/zynqmp_a53.dtsi?plain=1#L48">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P003_arm_gic-v2.md#std-dtcompatible-arm-gic-v2"><code>arm,gic-v2</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>片上（On-Chip）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/zynqmp_a53.dtsi?plain=1#L29">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Xilinx处理系统通用异步收发器（PS UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/zynqmp_a53.dtsi?plain=1#L57">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/zynqmp_a53.dtsi?plain=1#L65">已禁用：1</a>）</td>
<td><a href="../uart_ti_wch_virtual_binding_reference/P011_xlnx_xuartps.md#std-dtcompatible-xlnx-xuartps"><code>xlnx,xuartps</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/amd/zynqmp_apu/zynqmp_apu.dts?plain=1#L22">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="2">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>Xilinx处理系统三通道定时计数器（PS Triple-Timer Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/zynqmp_a53.dtsi?plain=1#L73">已禁用：4</a>）</td>
<td><a href="../mcu_timer_binding_reference/P014_xlnx_ttcps.md#std-dtcompatible-xlnx-ttcps"><code>xlnx,ttcps</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/xilinx/zynqmp_a53.dtsi?plain=1#L34">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

默认控制台为UART0，Linux中通常名为`ttyPS0`。

<a id="memories"></a>

#### 存储器（Memories）


- `sram0`使用低地址DDR窗口，从`0x0`开始，大小为2 GiB。

<a id="known-limitations"></a>

### 已知限制（Known Limitations）


- 此配置仅支持CPU0。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`zynqmp_apu`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
<th>调试服务器（debugserver）</th>
</tr>
<tr>
<td><a href="https://docs.zephyrproject.org/latest/develop/flash_debug/host-tools.html#runner-xsdb">xsdb</a></td>
<td>✅（默认 / default）</td>
<td>✅（默认 / default）</td>
<td>✅</td>
</tr>
</table>

构建示例：

```text
# From the root of the zephyr repository
west build -b zynqmp_apu samples/hello_world
```

<a id="arm-trusted-firmware-tf-a"></a>

### Arm可信固件（TF-A / Trusted Firmware）

启用`CONFIG_BUILD_WITH_TFA`时（此开发板默认启用），构建过程还会在`build/tfa/zynqmp/<release|debug>/bl31/`下生成TF-A的`bl31.elf`。在硬件上，平台固件（PDI中的比特流、第一阶段引导加载程序FSBL及电源管理单元固件PMUFW）和TF-A初始化处理系统（PS），并通过安全监控调用（SMC）提供电源状态协调接口（PSCI）后，Zephyr作为BL33运行。

AMD ZynqMP开发板不从`fip.bin`启动。构建TF-A时，将`PRELOADED_BL33_BASE`设置为设备树指定的Zephyr加载地址；XSDB运行工具（Runner）分别加载比特流（Bitstream）、FSBL、`bl31.elf`和Zephyr ELF。启用`CONFIG_BUILD_WITH_TFA`时，`west flash`会通过`--bl31`自动传递构建生成的`bl31.elf`路径。

<a id="references"></a>

## 参考资料（References）


1. AMD Zynq UltraScale+器件技术参考手册（Technical Reference Manual），UG1085

## 译注

官方自动生成目标表含smp目标，而限制段落仍写仅支持首个CPU；译文同时保留，未据此补造多核支持结论。

---

[上一章](P011_Versal_NET_RPU_development_board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_AMD_Zynq_UltraScale_MPSoC_RPU.md)
