---
id: learning.zephyr-docs.boards-amd.page-13
title: AMD Zynq UltraScale MPSoC RPU
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/amd/zynqmp_rpu/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="zynqmp_rpu"></a>

# 第13章\_AMD Zynq UltraScale+多处理器片上系统实时处理单元（MPSoC RPU）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/amd/zynqmp_rpu/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`zynqmp_rpu`

厂商（Vendor）：

[Advanced Micro Devices（AMD）, Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=amd)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)

片上系统（SoC）：

[`zynqmp_rpu`](https://docs.zephyrproject.org/latest/boards/index.html#soc=zynqmp_rpu)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/amd/zynqmp_rpu/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

此开发板配置面向AMD Zynq UltraScale+ MPSoC上的Cortex-R5实时处理单元（RPU）。R5 DDR从`0x00400000`开始，RPU的GIC地址为`0xf9000000`，处理系统UART0为`0xff000000`。

<a id="hardware"></a>

## 硬件（Hardware）

<a id="supported-features"></a>

### 支持的功能（Supported Features）

`zynqmp_rpu`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="zynqmp_rpu-hw-features"></a>

<a id="zynqmp_rpu-zynqmp_rpu/zynqmp_rpu-hw-features-section"></a>

#### `zynqmp_rpu/zynqmp_rpu`目标（Target）

<a id="zynqmp_rpu-zynqmp_rpu/zynqmp_rpu-hw-features-panel"></a>

<a id="zynqmp_rpu-zynqmp_rpu/zynqmp_rpu-hw-features-memory"></a>

该开发板目标的片上存储容量：64 MiB RAM、512 MiB Flash。

<a id="zynqmp_rpu-zynqmp_rpu/zynqmp_rpu-hw-features-table"></a>

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
<td>ARM Cortex-R5F处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp_rpu.dtsi?plain=1#L14">已启用：1</a>）</td>
<td><a href="../cpu_cortex_xtensa_binding_reference/P012_arm_cortex-r5f.md#std-dtcompatible-arm-cortex-r5f"><code>arm,cortex-r5f</code></a></td>
</tr>
<tr>
<td rowspan="1">计数器（Counter）</td>
<td>片上（On-Chip）</td>
<td>Xilinx Zynq UltraScale+ MPSoC实时时钟（RTC）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L353">已禁用：1</a>）</td>
<td><a href="../stm32_ti_xilinx_counter_binding_reference/P016_xlnx_zynqmp-rtc.md#std-dtcompatible-xlnx-zynqmp-rtc"><code>xlnx,zynqmp-rtc</code></a></td>
</tr>
<tr>
<td rowspan="1">错误检测与纠正（EDAC）</td>
<td>片上（On-Chip）</td>
<td>Xilinx ZynqMP双倍数据率存储器控制器（DDR Memory Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L309">已禁用：1</a>）</td>
<td><a href="../edac_syscon_binding_reference/P005_xlnx_zynqmp-ddrc-2.40a.md#std-dtcompatible-xlnx-zynqmp-ddrc-2.40a"><code>xlnx,zynqmp-ddrc-2.40a</code></a></td>
</tr>
<tr>
<td rowspan="2">以太网（Ethernet）</td>
<td>片上（On-Chip）</td>
<td>Xilinx千兆以太网媒体访问控制器（GEM Ethernet Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L101">已禁用：4</a>）</td>
<td><a href="../ethernet_synopsys_st_xilinx_binding_reference/P022_xlnx_gem.md#std-dtcompatible-xlnx-gem"><code>xlnx,gem</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Xilinx GEM管理数据输入输出节点（MDIO Node）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L123">已禁用：4</a>）</td>
<td><a href="../ethernet_mdio_microchip_binding_reference/P012_xlnx_gem-mdio.md#std-dtcompatible-xlnx-gem-mdio"><code>xlnx,gem-mdio</code></a></td>
</tr>
<tr>
<td rowspan="2">通用输入输出与接插件（GPIO &amp; Headers）</td>
<td>片上（On-Chip）</td>
<td>Xilinx Zynq-7000/ZynqMP MIO/EMIO通用输入输出控制器（GPIO Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L221">已启用：1</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P030_xlnx_ps-gpio.md#std-dtcompatible-xlnx-ps-gpio"><code>xlnx,ps-gpio</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Xilinx Zynq-7000/ZynqMP MIO/EMIO GPIO控制器组（Bank）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L232">已启用：6</a>）</td>
<td><a href="../gpio_ti_xilinx_sdl_binding_reference/P029_xlnx_ps-gpio-bank.md#std-dtcompatible-xlnx-ps-gpio-bank"><code>xlnx,ps-gpio-bank</code></a></td>
</tr>
<tr>
<td rowspan="1">集成电路间总线（I2C）</td>
<td>片上（On-Chip）</td>
<td>Cadence I2C控制器（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L287">已禁用：2</a>）</td>
<td><a href="../i2c_adi_atmel_esp_binding_reference/P015_cdns_i2c.md#std-dtcompatible-cdns-i2c"><code>cdns,i2c</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>片上（On-Chip）</td>
<td>ARM通用中断控制器（GIC）v1（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp_rpu.dtsi?plain=1#L100">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P002_arm_gic-v1.md#std-dtcompatible-arm-gic-v1"><code>arm,gic-v1</code></a></td>
</tr>
<tr>
<td rowspan="1">处理器间消息（IPM）</td>
<td>片上（On-Chip）</td>
<td>Xilinx处理器间中断（IPI / Inter Processor Interrupt）邮箱控制器（Mailbox Controller）用于管理两个Xilinx Zynq UltraScale+ MPSoC IPI代理（Agents）之间的消息传递（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp_rpu.dtsi?plain=1#L22">已禁用：2</a>）</td>
<td><a href="../intercore_reference/P076_ZynqMP处理器间中断邮箱绑定.md#dtbinding-xlnx-zynqmp-ipi-mailbox"><code>xlnx,zynqmp-ipi-mailbox</code></a></td>
</tr>
<tr>
<td rowspan="1">存储技术设备（MTD）</td>
<td>片上（On-Chip）</td>
<td>闪存（Flash）节点（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L19">已禁用：1</a>）</td>
<td><a href="../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash"><code>soc-nv-flash</code></a></td>
</tr>
<tr>
<td rowspan="1">引脚控制（Pin Control）</td>
<td>片上（On-Chip）</td>
<td>Xilinx ZynqMP片上系统引脚控制器（SoC Pin Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L14">已启用：1</a>）</td>
<td><a href="../pinctrl_stm32_ti_xilinx_binding_reference/P022_xlnx_pinctrl-zynqmp.md#std-dtcompatible-xlnx-pinctrl-zynqmp"><code>xlnx,pinctrl-zynqmp</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>片上（On-Chip）</td>
<td>Xilinx处理系统通用异步收发器（PS UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L31">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L40">已禁用：1</a>）</td>
<td><a href="../uart_ti_wch_virtual_binding_reference/P011_xlnx_xuartps.md#std-dtcompatible-xlnx-xuartps"><code>xlnx,xuartps</code></a></td>
</tr>
<tr>
<td rowspan="2">串行外设接口（SPI）</td>
<td>片上（On-Chip）</td>
<td>Cadence串行外设接口控制器（SPI Controller）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L317">已禁用：2</a>）</td>
<td><a href="../spi_adi_atmel_esp_binding_reference/P011_cdns_spi.md#std-dtcompatible-cdns-spi"><code>cdns,spi</code></a></td>
</tr>
<tr>
<td>片上（On-Chip）</td>
<td>Xilinx ZynqMP四线SPI接口（Quad SPI）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L343">已禁用：1</a>）</td>
<td><a href="../spi_stm32_ti_xilinx_binding_reference/P021_xlnx_zynqmp-qspi-1.0.md#std-dtcompatible-xlnx-zynqmp-qspi-1.0"><code>xlnx,zynqmp-qspi-1.0</code></a></td>
</tr>
<tr>
<td rowspan="1">静态随机存储器（SRAM）</td>
<td>板载（On-Board）</td>
<td>通用片上静态随机存储器（SRAM）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/amd/zynqmp_rpu/zynqmp_rpu.dts?plain=1#L14">已启用：1</a>）</td>
<td><a href="../hardware/P567_内存映射SRAM绑定.md#dtbinding-mmio-sram"><code>mmio-sram</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>片上（On-Chip）</td>
<td>Xilinx处理系统三通道定时计数器（PS Triple-Timer Counter）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L49">已启用：1</a>；<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L62">已禁用：3</a>）</td>
<td><a href="../mcu_timer_binding_reference/P014_xlnx_ttcps.md#std-dtcompatible-xlnx-ttcps"><code>xlnx,ttcps</code></a></td>
</tr>
</table>

默认控制台为UART0，Linux中通常名为`ttyPS0`。

<a id="memories"></a>

#### 存储器（Memories）


- `sram0`位于`0x0400_0000`，即64 MiB。
- QSPI线性闪存（Linear Flash）映射到`0xc0000000`，容量512 MiB。

<a id="known-limitations"></a>

### 已知限制（Known Limitations）


- 此开发板文件不面向双冗余锁步R5运行（Dual-Redundant Lock-Step）。
- 仅支持第一个R5内核。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

`zynqmp_rpu`开发板支持下表所列的运行工具（Runners）及相关west命令。

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

<a id="qemu"></a>

### QEMU

开发板使用`arm-generic-fdt` QEMU机器模型，构建时从`zynqmp_rpu-qemu.dts`编译ZCU102硬件设备树二进制文件（DTB）。Zephyr ELF加载到`cpu-num=4`，即R5集群；向`0xff5e023c`和`0xff9a0000`进行内存映射输入输出（MMIO）写操作，以解除R5复位。

```text
west build -b zynqmp_rpu samples/hello_world
west build -t run
```

<a id="hardware-xsdb"></a>

### 硬件部署（XSDB）

```text
# From the root of the zephyr repository
west build -b zynqmp_rpu samples/hello_world
```

<a id="references"></a>

## 参考资料（References）


1. AMD Zynq UltraScale+器件技术参考手册（Technical Reference Manual），UG1085

## 译注

原文概述的R5 DDR起始地址写作0x00400000，后文sram0地址写作0x0400_0000。两处数值不同，译文分别保留，不将其当成已经核对一致的存储器布局。

---

[上一章](P012_AMD_Zynq_UltraScale_MPSoC_APU.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
