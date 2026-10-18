---
id: learning.zephyr-docs.qemu-arm-reference.page-3
title: QEMU_Cortex_M0仿真开发板
kind: reference
status: maintained
domains: [zephyr, boards, qemu]
source_url: https://docs.zephyrproject.org/latest/boards/qemu/cortex_m0/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_QEMU\_Cortex\_M0仿真开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qemu/cortex_m0/doc/index.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="qemu_cortex_m0"></a>

## 3.1\_开发板概况

名称：`qemu_cortex_m0`。厂商：[Nordic Semiconductor](https://docs.zephyrproject.org/latest/boards/index.html#vendor=nordic)。维护状态：持续维护（Maintained）。架构（Architecture）：[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)；片上系统（SoC）：[nrf51822](https://docs.zephyrproject.org/latest/boards/index.html#soc=nrf51822)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/boards/qemu/cortex_m0)。

<a id="overview"></a>

此开发板配置使用 QEMU 仿真 BBC Microbit（Nordic nRF51822）平台。配置支持 ARM Cortex-M0 CPU 以及嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC）和 TIMER（nRF TIMER 系统时钟，System Clock）。

> 原文注意：此开发板配置不声称适用于实际的 nRF51 Microbit 硬件系统或任何其他硬件系统。

<a id="hardware"></a>

## 3.2\_硬件与支持特性

<a id="supported-features"></a>

<a id="qemu_cortex_m0-hw-features"></a>

`qemu_cortex_m0` 支持下表列出的硬件特性（Supported Features）。

“片上（on-chip）”表示特性集成于 SoC，“板上（on-board）”表示特性位于开发板。启用／禁用两列分别保留官方页面的实例计数（Enabled/Disabled Instance Count）；数字链接指向开发板或 SoC 设备树源码（DTS）中相应状态的第一个实例。兼容字符串（Compatible String，如 `vnd,foo`）链接指向对应设备树绑定文档。RAM 指随机存取存储器，Flash 指闪存；KiB、MiB 分别为二进制千字节、兆字节。

<a id="qemu_cortex_m0-qemu_cortex_m0/nrf51822-hw-features-section"></a>

<a id="qemu_cortex_m0-qemu_cortex_m0/nrf51822-hw-features-panel"></a>

<a id="qemu_cortex_m0-qemu_cortex_m0/nrf51822-hw-features-memory"></a>

<a id="qemu_cortex_m0-qemu_cortex_m0/nrf51822-hw-features-table"></a>

### 3.2.1\_目标 `qemu_cortex_m0/nrf51822`

目标存储容量：RAM 为 16 KiB，Flash 为 256 KiB。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 中央处理器（Central Processing Unit，CPU） | 片上（on-chip） | ARM Cortex-M0 中央处理器（CPU） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L22) | — | [`arm,cortex-m0`](../cpu_arm_riscv_binding_reference/P018_arm_cortex-m0.md#std-dtcompatible-arm-cortex-m0) |
| 模数转换器（Analog-to-Digital Converter，ADC） | 片上（on-chip） | nRF 模数转换器节点（ADC Node） | — | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L178) | [`nordic,nrf-adc`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/adc/nordic%2Cnrf-adc.html#std-dtcompatible-nordic-nrf-adc) |
| ARM 架构（ARM Architecture） | 片上（on-chip） | Nordic 用户信息配置寄存器（User Information Configuration Registers，UICR） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L48) | — | [`nordic,nrf-uicr`](../arm_nordic_nxp_control_binding_reference/P007_nordic_nrf-uicr.md#std-dtcompatible-nordic-nrf-uicr) |
| ARM 架构（ARM Architecture） | 片上（on-chip） | Nordic nRF 系列内存保护单元（Memory Protection Unit，MPU） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L97) | — | [`nordic,nrf-mpu`](../arm_timing_ethosu_control_binding_reference/P020_nordic_nrf-mpu.md#std-dtcompatible-nordic-nrf-mpu) |
| ARM 架构（ARM Architecture） | 片上（on-chip） | Nordic nRF 系列软件中断（Software Interrupt，SWI） | [6](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L286) | — | [`nordic,nrf-swi`](../arm_nordic_nxp_control_binding_reference/P005_nordic_nrf-swi.md#std-dtcompatible-nordic-nrf-swi) |
| 时钟控制（Clock Control） | 片上（on-chip） | Nordic nRF 时钟控制节点（Clock Control Node） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L80) | — | [`nordic,nrf-clock`](../clock_sam_nordic_binding_reference/P015_nordic_nrf-clock.md#std-dtcompatible-nordic-nrf-clock) |
| 时钟控制（Clock Control） | 片上（on-chip） | Nordic nRF 高频时钟控制节点（HFCLK Clock Control Node） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L86) | — | [`nordic,nrf-clock-hfclk`](../clock_sam_nordic_binding_reference/P009_nordic_nrf-clock-hfclk.md#std-dtcompatible-nordic-nrf-clock-hfclk) |
| 时钟控制（Clock Control） | 片上（on-chip） | Nordic nRF 低频时钟控制节点（LFCLK Clock Control Node） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L91) | — | [`nordic,nrf-clock-lfclk`](../clock_sam_nordic_binding_reference/P012_nordic_nrf-clock-lfclk.md#std-dtcompatible-nordic-nrf-clock-lfclk) |
| 时钟控制（Clock Control） | 片上（on-chip） | Nordic nRF 高频晶体振荡器（High-frequency Crystal Oscillator），用于 nRF51 系列 | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L30) | — | [`nordic,nrf51-hfxo`](../clock_sam_nordic_binding_reference/P021_nordic_nrf51-hfxo.md#std-dtcompatible-nordic-nrf51-hfxo) |
| 比较器（Comparator） | 片上（on-chip） | Nordic nRF 模拟低功耗比较器（Low-Power Comparator，LPCOMP） | — | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L278) | [`nordic,nrf-lpcomp`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/nordic%2Cnrf-lpcomp.html#std-dtcompatible-nordic-nrf-lpcomp) |
| 计数器（Counter） | 片上（on-chip） | Nordic nRF 定时器节点（Timer Node） | — | [3](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L186) | [`nordic,nrf-timer`](../microchip_soc_counter_binding_reference/P017_nordic_nrf-timer.md#std-dtcompatible-nordic-nrf-timer) |
| 密码加速器（Cryptographic Accelerator） | 片上（on-chip） | Nordic ECB：高级加密标准（AES）的电子密码本模式加密（Electronic Codebook Mode） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L240) | — | [`nordic,nrf-ecb`](../crypto_secure_engine_st_ti_binding_reference/P001_nordic_nrf-ecb.md#std-dtcompatible-nordic-nrf-ecb) |
| 密码加速器（Cryptographic Accelerator） | 片上（on-chip） | Nordic nRF 系列 CCM：AES CCM 模式加密（AES CCM Mode Encryption） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L247) | — | [`nordic,nrf-ccm`](../crypto_aes_sha_ccm_binding_reference/P020_nordic_nrf-ccm.md#std-dtcompatible-nordic-nrf-ccm) |
| 闪存控制器（Flash Controller） | 片上（on-chip） | Nordic 非易失性存储器控制器（Non-Volatile Memory Controller，NVMC） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L328) | — | [`nordic,nrf51-flash-controller`](../flash_adi_microchip_nordic_binding_reference/P029_nordic_nrf51-flash-controller.md#std-dtcompatible-nordic-nrf51-flash-controller) |
| 通用输入输出与接针（GPIO & Headers） | 片上（on-chip） | NRF5 GPIO 任务与事件（GPIO Tasks and Events，GPIOTE） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L170) | — | [`nordic,nrf-gpiote`](../gpio_microchip_nordic_nuvoton_binding_reference/P017_nordic_nrf-gpiote.md#std-dtcompatible-nordic-nrf-gpiote) |
| 通用输入输出与接针（GPIO & Headers） | 片上（on-chip） | NRF5 通用输入输出（GPIO） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L351) | — | [`nordic,nrf-gpio`](../gpio_microchip_nordic_nuvoton_binding_reference/P016_nordic_nrf-gpio.md#std-dtcompatible-nordic-nrf-gpio) |
| 集成电路间总线（Inter-Integrated Circuit，I2C） | 片上（on-chip） | Nordic nRF 系列双线接口主控制器（Two-Wire Interface，TWI Master） | — | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L133) | [`nordic,nrf-twi`](../i2c_infineon_ite_nordic_binding_reference/P015_nordic_nrf-twi.md#std-dtcompatible-nordic-nrf-twi) |
| 中断控制器（Interrupt Controller） | 片上（on-chip） | ARMv6-M 嵌套向量中断控制器（Nested Vectored Interrupt Controller，NVIC） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | — | [`arm,v6m-nvic`](../arm_interrupt_timer_binding_reference/P001_ARMv6_M_NVIC.md#std-dtcompatible-arm-v6m-nvic) |
| 杂项（Miscellaneous） | 片上（on-chip） | Nordic 工厂信息配置寄存器（Factory Information Configuration Registers，FICR） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L41) | — | [`nordic,nrf-ficr`](../misc_adi_nordic_binding_reference/P018_nordic_nrf-ficr.md#std-dtcompatible-nordic-nrf-ficr) |
| 杂项（Miscellaneous） | 片上（on-chip） | Nordic nRF 系列可编程外设互连（Programmable Peripheral Interconnect，PPI） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L345) | — | [`nordic,nrf-ppi`](../misc_adi_nordic_binding_reference/P020_nordic_nrf-ppi.md#std-dtcompatible-nordic-nrf-ppi) |
| 存储技术设备（Memory Technology Device，MTD） | 片上（on-chip） | 闪存节点（Flash Node） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L335) | — | [`soc-nv-flash`](../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| 网络（Networking） | 片上（on-chip） | Nordic nRF 系列无线电外设（RADIO Peripheral） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L103) | — | [`nordic,nrf-radio`](../network_radio_frontend_binding_reference/P009_nordic_nrf-radio.md#std-dtcompatible-nordic-nrf-radio) |
| 引脚控制（Pin Control） | 片上（on-chip） | Nordic nRF 系列引脚控制器（Pin Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L26) | — | [`nordic,nrf-pinctrl`](../pinctrl_infineon_nordic_nxp_binding_reference/P009_nordic_nrf-pinctrl.md#std-dtcompatible-nordic-nrf-pinctrl) |
| 电源管理（Power Management） | 片上（on-chip） | Nordic nRF 电源控制节点（Power Control Node） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L63) | — | [`nordic,nrf-power`](../power_control_binding_reference/P008_nordic_nrf-power.md#std-dtcompatible-nordic-nrf-power) |
| 脉宽调制（Pulse Width Modulation，PWM） | 片上（on-chip） | nRFx 软件脉宽调制（Software PWM） | — | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/vendor/nordic/nrf_common.dtsi?plain=1#L39) | [`nordic,nrf-sw-pwm`](../pwm_intel_microchip_nxp_binding_reference/P016_nordic_nrf-sw-pwm.md#std-dtcompatible-nordic-nrf-sw-pwm) |
| 保持存储器（Retained Memory） | 片上（on-chip） | Nordic 通用寄存器保持设备（General Purpose Register Retention，GPREGRET） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L71) | — | [`nordic,nrf-gpregret`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/retained_mem/nordic%2Cnrf-gpregret.html#std-dtcompatible-nordic-nrf-gpregret) |
| 随机数发生器（Random Number Generator，RNG） | 片上（on-chip） | Nordic nRF 系列随机数发生器（Random Number Generator，RNG） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L233) | — | [`nordic,nrf-rng`](../rng_binding_reference/P014_nordic_nrf-rng.md#std-dtcompatible-nordic-nrf-rng) |
| 实时时钟／计数器（RTC） | 片上（on-chip） | Nordic nRF 实时计数器（Real-Time Counter，RTC） | — | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L216) | [`nordic,nrf-rtc`](../microchip_microcrystal_nxp_rtc_binding_reference/P010_nordic_nrf-rtc.md#std-dtcompatible-nordic-nrf-rtc) |
| 传感器（Sensors） | 片上（on-chip） | Nordic nRF 系列温度节点（TEMP Node） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L226) | — | [`nordic,nrf-temp`](../sensor_microchip_nordic_nxp_binding_reference/P023_nordic_nrf-temp.md#std-dtcompatible-nordic-nrf-temp) |
| 传感器（Sensors） | 片上（on-chip） | Nordic nRF 正交解码器节点（Quadrature Decoder，QDEC） | — | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L271) | [`nordic,nrf-qdec`](../sensor_microchip_nordic_nxp_binding_reference/P021_nordic_nrf-qdec.md#std-dtcompatible-nordic-nrf-qdec) |
| 串行控制器（Serial Controller） | 片上（on-chip） | Nordic nRF 系列通用异步收发器（UART） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L115) | — | [`nordic,nrf-uart`](../uart_microchip_nordic_nxp_binding_reference/P003_nordic_nrf-uart.md#std-dtcompatible-nordic-nrf-uart) |
| 串行外设接口（Serial Peripheral Interface，SPI） | 片上（on-chip） | Nordic nRF 系列 SPI 控制器（SPI Controller） | — | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L122) | [`nordic,nrf-spi`](../spi_microchip_nordic_nxp_binding_reference/P012_nordic_nrf-spi.md#std-dtcompatible-nordic-nrf-spi) |
| 静态随机存取存储器（Static Random-Access Memory，SRAM） | 片上（on-chip） | 通用片上 SRAM（Generic On-chip SRAM） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L57) | — | [`mmio-sram`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sram/mmio-sram.html#std-dtcompatible-mmio-sram) |
| 看门狗（Watchdog） | 片上（on-chip） | Nordic nRF 系列看门狗定时器（Watchdog Timer，WDT） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nordic/nrf51822.dtsi?plain=1#L254) | — | [`nordic,nrf-wdt`](../nxp_nordic_nuvoton_watchdog_binding_reference/P002_nordic_nrf-wdt.md#std-dtcompatible-nordic-nrf-wdt) |

<a id="devices"></a>

## 3.3\_设备

<a id="system-clock"></a>

### 3.3.1\_系统时钟

此配置使用 1 MHz 的系统时钟频率（System Clock Frequency）。

<a id="serial-port"></a>

### 3.3.2\_串口

此配置通过CPU 的 UART0 使用单个串行通信通道（Serial Communication Channel）。

<a id="known-problems-or-limitations"></a>

### 3.3.3\_已知问题与限制

以下平台特性不受支持：

- 写入硬件闪存（Flash Memory）。

<a id="programming-and-debugging"></a>

## 3.4\_编程与调试

`qemu_cortex_m0` 支持以下运行器（Runner）及对应 west 命令：

| 运行器 | `west flash` | `west debug` | `west debugserver` |
| --- | --- | --- | --- |
| `qemu` | 支持，默认 | 支持，默认 | 支持 |

可用此配置在 QEMU 仿真环境中运行基本 Zephyr 应用及内核测试。以下以[基础同步示例（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)为例，从 Zephyr 仓库根目录执行（代码注释 `From the root of the zephyr repository` 也表示这一位置）：

```shell
# From the root of the zephyr repository
west build -b qemu_cortex_m0 samples/synchronization
west build -t run
```

这会构建包含同步示例应用的镜像（Image），使用 QEMU 启动，并显示以下控制台输出（Console Output）：

```text
***** BOOTING ZEPHYR OS v1.8.99 - BUILD: Jun 27 2017 13:09:26 *****
threadA: Hello World from arm!
threadB: Hello World from arm!
threadA: Hello World from arm!
threadB: Hello World from arm!
threadA: Hello World from arm!
threadB: Hello World from arm!
threadA: Hello World from arm!
threadB: Hello World from arm!
threadA: Hello World from arm!
threadB: Hello World from arm!
```

按 `CTRL+A`，再按 `x` 退出 QEMU。

> 译注：输出是官方页面给出的示例，版本字符串按原样保留；本次翻译没有运行固件或重新生成这些输出。

<a id="debugging"></a>

### 3.4.1\_调试

详细概述参见[应用调试（Application Debugging）](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

<a id="networking"></a>

### 3.4.2\_网络

原文此节没有提供说明。

<a id="references"></a>

## 3.5\_参考资料

1. Joseph Yiu 著《ARM Cortex-M0 权威指南》，第二版（The Definitive Guide to the ARM Cortex-M0, Second Edition by Joseph Yiu (ISBN 978-0-12-803278-7)）。
2. ARM 架构技术参考手册（ARMv6-M Architecture Technical Reference Manual (ARM DDI 0419D 0403D ID051917)）。
3. ARM 架构过程调用标准（Procedure Call Standard for the ARM Architecture (ARM IHI 0042E, current through ABI release 2.09, 2012/11/30)）。
4. Cortex-M0 r2p1 版技术参考手册（Cortex-M0 Revision r2p1 Technical Reference Manual (ARM DDI 0432C ID113009)）。
5. Cortex-M0 器件通用用户指南（Cortex-M0 Devices Generic User Guide (ARM DUI 0497A ID112109)）。

---

[上一章](P002_QEMU_Cortex_A72仿真开发板.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md) · [下一章](P004_QEMU_Cortex_M3仿真开发板.md)
