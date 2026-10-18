---
id: learning.zephyr-docs.qemu-arm-reference.page-5
title: QEMU_Cortex_R5仿真开发板
kind: reference
status: maintained
domains: [zephyr, boards, qemu]
source_url: https://docs.zephyrproject.org/latest/boards/qemu/cortex_r5/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_QEMU\_Cortex\_R5仿真开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qemu/cortex_r5/doc/index.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="qemu_cortex_r5"></a>

## 5.1\_开发板概况

名称：`qemu_cortex_r5`。厂商：[QEMU，通用开源机器仿真器与虚拟化器](https://docs.zephyrproject.org/latest/boards/index.html#vendor=qemu)。维护状态：未积极维护（Not Actively Maintained）。架构（Architecture）：[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)；片上系统（SoC）：[zynqmp_rpu](https://docs.zephyrproject.org/latest/boards/index.html#soc=zynqmp_rpu)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/boards/qemu/cortex_r5)。

<a id="overview"></a>

此开发板配置使用 QEMU 仿真 Xilinx Zynq UltraScale+（ZynqMP）平台。配置支持 ARM Cortex-R5 CPU，以及 ARM PL-390 通用中断控制器（Generic Interrupt Controller）、Xilinx Zynq 三重定时计数器（Triple-Timer Counter，TTC；Cadence TTC）和 Xilinx Zynq UART。

> 原文注意：此开发板配置不声称适用于实际的 ZCU102 硬件系统或任何其他硬件系统。

<a id="hardware"></a>

## 5.2\_硬件与支持特性

<a id="supported-features"></a>

<a id="qemu_cortex_r5-hw-features"></a>

`qemu_cortex_r5` 支持下表列出的硬件特性（Supported Features）。

“片上（on-chip）”表示特性集成于 SoC，“板上（on-board）”表示特性位于开发板。启用／禁用两列分别保留官方页面的实例计数（Enabled/Disabled Instance Count）；数字链接指向开发板或 SoC 设备树源码（DTS）中相应状态的第一个实例。兼容字符串（Compatible String，如 `vnd,foo`）链接指向对应设备树绑定文档。RAM 指随机存取存储器，Flash 指闪存；KiB、MiB 分别为二进制千字节、兆字节。

<a id="qemu_cortex_r5-qemu_cortex_r5/zynqmp_rpu-hw-features-section"></a>

<a id="qemu_cortex_r5-qemu_cortex_r5/zynqmp_rpu-hw-features-panel"></a>

<a id="qemu_cortex_r5-qemu_cortex_r5/zynqmp_rpu-hw-features-memory"></a>

<a id="qemu_cortex_r5-qemu_cortex_r5/zynqmp_rpu-hw-features-table"></a>

### 5.2.1\_目标 `qemu_cortex_r5/zynqmp_rpu`

目标存储容量：RAM 为 64 MiB，Flash 为 32 MiB。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 中央处理器（Central Processing Unit，CPU） | 片上（on-chip） | ARM Cortex-R5F 中央处理器（CPU） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp_rpu.dtsi?plain=1#L14) | — | [`arm,cortex-r5f`](../cpu_cortex_xtensa_binding_reference/P012_arm_cortex-r5f.md#std-dtcompatible-arm-cortex-r5f) |
| 计数器（Counter） | 片上（on-chip） | Xilinx Zynq UltraScale+ 多处理器片上系统实时时钟（MPSoC Real Time Clock） | — | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L353) | [`xlnx,zynqmp-rtc`](../stm32_ti_xilinx_counter_binding_reference/P016_xlnx_zynqmp-rtc.md#std-dtcompatible-xlnx-zynqmp-rtc) |
| 错误检测与纠正（Error Detection and Correction，EDAC） | 片上（on-chip） | Xilinx ZynqMP 双倍数据速率存储器控制器（DDR Memory Controller） | — | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L309) | [`xlnx,zynqmp-ddrc-2.40a`](../edac_syscon_binding_reference/P005_xlnx_zynqmp-ddrc-2.40a.md#std-dtcompatible-xlnx-zynqmp-ddrc-2.40a) |
| 以太网（Ethernet） | 片上（on-chip） | Xilinx GEM 以太网控制器（Ethernet Controller） | — | [4](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L101) | [`xlnx,gem`](../ethernet_synopsys_st_xilinx_binding_reference/P022_xlnx_gem.md#std-dtcompatible-xlnx-gem) |
| 以太网（Ethernet） | 片上（on-chip） | Xilinx GEM 管理数据输入输出节点（MDIO Node） | — | [4](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L123) | [`xlnx,gem-mdio`](../ethernet_mdio_microchip_binding_reference/P012_xlnx_gem-mdio.md#std-dtcompatible-xlnx-gem-mdio) |
| 通用输入输出与接针（GPIO & Headers） | 片上（on-chip） | Xilinx Zynq-7000/ZynqMP MIO/EMIO 通用输入输出控制器（GPIO Controller） | — | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L221) | [`xlnx,ps-gpio`](../gpio_ti_xilinx_sdl_binding_reference/P030_xlnx_ps-gpio.md#std-dtcompatible-xlnx-ps-gpio) |
| 通用输入输出与接针（GPIO & Headers） | 片上（on-chip） | Xilinx Zynq-7000/ZynqMP MIO/EMIO 通用输入输出控制器组（GPIO Controller Bank） | [6](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L232) | — | [`xlnx,ps-gpio-bank`](../gpio_ti_xilinx_sdl_binding_reference/P029_xlnx_ps-gpio-bank.md#std-dtcompatible-xlnx-ps-gpio-bank) |
| 集成电路间总线（Inter-Integrated Circuit，I2C） | 片上（on-chip） | Cadence I2C 控制器（I2C Controller） | — | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L287) | [`cdns,i2c`](../i2c_adi_atmel_esp_binding_reference/P015_cdns_i2c.md#std-dtcompatible-cdns-i2c) |
| 中断控制器（Interrupt Controller） | 片上（on-chip） | ARM 通用中断控制器第1版（Generic Interrupt Controller v1，GICv1） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp_rpu.dtsi?plain=1#L100) | — | [`arm,gic-v1`](../interrupt_fabric_binding_reference/P002_arm_gic-v1.md#std-dtcompatible-arm-gic-v1) |
| 处理器间消息（Inter-Processor Messaging，IPM） | 片上（on-chip） | Xilinx 处理器间中断（Inter Processor Interrupt，IPI）邮箱控制器：管理两个 Xilinx Zynq UltraScale+ MPSoC IPI 代理之间的消息传递 | — | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp_rpu.dtsi?plain=1#L22) | [`xlnx,zynqmp-ipi-mailbox`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/ipm/xlnx%2Czynqmp-ipi-mailbox.html#std-dtcompatible-xlnx-zynqmp-ipi-mailbox) |
| 存储技术设备（Memory Technology Device，MTD） | 片上（on-chip） | 闪存节点（Flash Node） | — | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L19) | [`soc-nv-flash`](../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| 存储技术设备（Memory Technology Device，MTD） | 板上（on-board） | 支持 Zephyr spi-nor 闪存驱动通过 Zephyr SPI 应用程序编程接口（API），使用基于标准 M25P80 的命令集控制串行闪存的属性 | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_r5/qemu_cortex_r5.dts?plain=1#L44) | — | [`jedec,spi-nor`](../mtd_microchip_nordic_nxp_binding_reference/P002_jedec_spi-nor.md#std-dtcompatible-jedec-spi-nor) |
| 引脚控制（Pin Control） | 片上（on-chip） | Xilinx ZynqMP 片上系统引脚控制器（SoC Pin Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L14) | — | [`xlnx,pinctrl-zynqmp`](../pinctrl_stm32_ti_xilinx_binding_reference/P022_xlnx_pinctrl-zynqmp.md#std-dtcompatible-xlnx-pinctrl-zynqmp) |
| 串行控制器（Serial Controller） | 片上（on-chip） | Xilinx 处理系统通用异步收发器（PS UART） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L31) | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L40) | [`xlnx,xuartps`](../uart_ti_wch_virtual_binding_reference/P011_xlnx_xuartps.md#std-dtcompatible-xlnx-xuartps) |
| 串行外设接口（Serial Peripheral Interface，SPI） | 片上（on-chip） | Cadence SPI 控制器（SPI Controller） | — | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L317) | [`cdns,spi`](../spi_adi_atmel_esp_binding_reference/P011_cdns_spi.md#std-dtcompatible-cdns-spi) |
| 串行外设接口（Serial Peripheral Interface，SPI） | 片上（on-chip） | Xilinx ZynqMP 四线 SPI 接口（Quad SPI Interface） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L343) | — | [`xlnx,zynqmp-qspi-1.0`](../spi_stm32_ti_xilinx_binding_reference/P021_xlnx_zynqmp-qspi-1.0.md#std-dtcompatible-xlnx-zynqmp-qspi-1.0) |
| 静态随机存取存储器（Static Random-Access Memory，SRAM） | 板上（on-board） | 通用片上 SRAM（Generic On-chip SRAM） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/qemu/cortex_r5/qemu_cortex_r5.dts?plain=1#L15) | — | [`mmio-sram`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sram/mmio-sram.html#std-dtcompatible-mmio-sram) |
| 定时器（Timer） | 片上（on-chip） | Xilinx 处理系统三重定时计数器（PS Triple-Timer Counter） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L49) | [3](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/xilinx/zynqmp.dtsi?plain=1#L62) | [`xlnx,ttcps`](../mcu_timer_binding_reference/P014_xlnx_ttcps.md#std-dtcompatible-xlnx-ttcps) |

<a id="devices"></a>

## 5.3\_设备

<a id="system-timer"></a>

### 5.3.1\_系统定时器

此配置使用 1000 Hz 的系统定时器节拍频率（System Timer Tick Frequency）。

<a id="serial-port"></a>

### 5.3.2\_串口

此配置通过片上 UART0 使用单个串行通信通道（Serial Communication Channel）。

<a id="known-problems-or-limitations"></a>

### 5.3.3\_已知问题与限制

以下平台特性不受支持：

- 未仿真双冗余核心锁步（Dual-redundant Core Lock-step，DCLS）执行。
- Xilinx Zynq TTC 驱动不支持无节拍（Tickless）模式运行。

<a id="programming-and-debugging"></a>

## 5.4\_编程与调试

`qemu_cortex_r5` 支持以下运行器（Runner）及对应 west 命令：

| 运行器 | `west flash` | `west debug` | `west debugserver` |
| --- | --- | --- | --- |
| `qemu` | 支持，默认 | 支持，默认 | 支持 |

可用此配置在 QEMU 仿真环境中运行基本 Zephyr 应用及内核测试。以下以[基础同步示例（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)为例，从 Zephyr 仓库根目录执行（代码注释 `From the root of the zephyr repository` 也表示这一位置）：

```shell
# From the root of the zephyr repository
west build -b qemu_cortex_r5 samples/synchronization
west build -t run
```

这会构建包含同步示例应用的镜像（Image），使用 QEMU 启动，并显示以下控制台输出（Console Output）：

```text
*** Booting Zephyr OS build v2.2.0  ***
threadA: Hello World from qemu_cortex_r5!
threadB: Hello World from qemu_cortex_r5!
threadA: Hello World from qemu_cortex_r5!
threadB: Hello World from qemu_cortex_r5!
threadA: Hello World from qemu_cortex_r5!
threadB: Hello World from qemu_cortex_r5!
threadA: Hello World from qemu_cortex_r5!
threadB: Hello World from qemu_cortex_r5!
threadA: Hello World from qemu_cortex_r5!
threadB: Hello World from qemu_cortex_r5!
```

按 `CTRL+A`，再按 `x` 退出 QEMU。

> 译注：输出是官方页面给出的示例，版本字符串按原样保留；本次翻译没有运行固件或重新生成这些输出。

<a id="debugging"></a>

### 5.4.1\_调试

详细概述参见[应用调试（Application Debugging）](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

<a id="references"></a>

## 5.5\_参考资料

1. ARMv7-A 与 ARMv7-R 架构参考手册（ARMv7-A and ARMv7-R Architecture Reference Manual (ARM DDI 0406C ID051414)）。
2. Cortex-R5 与 Cortex-R5F 技术参考手册（Cortex-R5 and Cortex-R5F Technical Reference Manual (ARM DDI 0460C ID021511)）。
3. Zynq UltraScale+ 器件技术参考手册（Zynq UltraScale+ Device Technical Reference Manual (UG1085)）。

---

[上一章](P004_QEMU_Cortex_M3仿真开发板.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md) · [下一章](P006_QEMU_AArch64_Virt_KVM仿真开发板.md)
