---
id: learning.zephyr-docs.qemu-arm-reference.page-2
title: QEMU_Cortex_A72仿真开发板
kind: reference
status: maintained
domains: [zephyr, boards, qemu]
source_url: https://docs.zephyrproject.org/latest/boards/qemu/cortex_a72/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_QEMU\_Cortex\_A72仿真开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qemu/cortex_a72/doc/index.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="qemu_cortex_a72"></a>

## 2.1\_开发板概况

名称：`qemu_cortex_a72`。厂商：[Raspberry Pi Foundation](https://docs.zephyrproject.org/latest/boards/index.html#vendor=raspberrypi)。维护状态：未积极维护（Not Actively Maintained）。架构（Architecture）：[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)；片上系统（SoC）：[bcm2711](https://docs.zephyrproject.org/latest/boards/index.html#soc=bcm2711)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/boards/qemu/cortex_a72)。

<a id="overview"></a>

此开发板配置使用 QEMU 仿真基于 Broadcom BCM2711 片上系统（System on Chip，SoC）的 Raspberry Pi 4B 硬件平台。配置支持 ARM Cortex-A72 CPU 及以下设备：

- ARM 架构定时器（Architected Timer）。
- ARM GIC-400 中断控制器。
- ARM PL011 通用异步收发器（UART）控制器。
- Broadcom BCM2835 辅助 UART（AUX UART）控制器。
- Broadcom BCM2835 时钟／复位管理器（Clock/Reset Manager，CPRMAN）。
- Broadcom BCM2835 直接存储器访问（DMA）控制器。
- Broadcom BCM2835 帧缓冲（Framebuffer）控制器。
- Broadcom BCM2835 通用输入输出（GPIO）控制器。
- Broadcom BCM2835 硬件随机数发生器（Hardware Random Number Generator）。
- Broadcom BCM2835 I2C（BSC）控制器。
- Broadcom BCM2835 邮箱（Mailbox）控制器。
- Broadcom BCM2835 安全数字卡／多媒体卡（SD/MMC）主控制器。
- Broadcom BCM2835 串行外设接口（SPI）控制器。
- Broadcom BCM2835 系统定时器（System Timer）。
- Broadcom BCM2835 温度传感器（Thermal Sensor）。
- Broadcom BCM2835 通用串行总线（USB）主控制器。
- Raspberry Pi VideoCore 固件属性接口（Firmware Property Interface）。
- Synopsys DWC2 USB2 主控制器。

<a id="hardware"></a>

## 2.2\_硬件与支持特性

<a id="supported-features"></a>

<a id="qemu_cortex_a72-hw-features"></a>

`qemu_cortex_a72` 支持下表列出的硬件特性（Supported Features）。

“片上（on-chip）”表示特性集成于 SoC，“板上（on-board）”表示特性位于开发板。启用／禁用两列分别保留官方页面的实例计数（Enabled/Disabled Instance Count）；数字链接指向开发板或 SoC 设备树源码（DTS）中相应状态的第一个实例。兼容字符串（Compatible String，如 `vnd,foo`）链接指向对应设备树绑定文档。RAM 指随机存取存储器，Flash 指闪存；KiB、MiB 分别为二进制千字节、兆字节。

<a id="qemu_cortex_a72-qemu_cortex_a72/bcm2711-hw-features-section"></a>

<a id="qemu_cortex_a72-qemu_cortex_a72/bcm2711-hw-features-panel"></a>

<a id="qemu_cortex_a72-qemu_cortex_a72/bcm2711-hw-features-memory"></a>

<a id="qemu_cortex_a72-qemu_cortex_a72/bcm2711-hw-features-table"></a>

### 2.2.1\_目标 `qemu_cortex_a72/bcm2711`

目标存储容量：RAM 为 8 MiB，Flash 为 不适用（N/A）。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 中央处理器（Central Processing Unit，CPU） | 片上（on-chip） | ARM Cortex-A72 中央处理器（CPU） | [4](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L23) | — | [`arm,cortex-a72`](../cpu_arm_riscv_binding_reference/P012_arm_cortex-a72.md#std-dtcompatible-arm-cortex-a72) |
| 时钟控制（Clock Control） | 片上（on-chip） | 通用固定频率时钟提供者（Generic Fixed-rate Clock Provider） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L67) | — | [`fixed-clock`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/fixed-clock.html#std-dtcompatible-fixed-clock) |
| 显示（Display） | 板上（on-board） | Raspberry Pi BCM2711 帧缓冲显示设备（Framebuffer Display Device） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L94) | — | [`raspberrypi,bcm2711-framebuffer`](../display_panel_renesas_sharp_binding_reference/P006_raspberrypi_bcm2711-framebuffer.md#std-dtcompatible-raspberrypi-bcm2711-framebuffer) |
| 以太网（Ethernet） | 片上（on-chip） | Broadcom GENET 千兆以太网控制器（Gigabit Ethernet Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L293) | — | [`brcm,genet`](../ethernet_mac_mdio_binding_reference/P006_brcm_genet.md#std-dtcompatible-brcm-genet) |
| 以太网（Ethernet） | 片上（on-chip） | Broadcom GENET 管理数据输入输出控制器（Management Data Input/Output，MDIO） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L302) | — | [`brcm,genet-mdio`](../ethernet_mac_mdio_binding_reference/P017_brcm_genet-mdio.md#std-dtcompatible-brcm-genet-mdio) |
| 以太网（Ethernet） | 板上（on-board） | 通用介质无关接口物理层器件（MII PHY） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L152) | — | [`ethernet-phy`](../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| 固件（Firmware） | 板上（on-board） | Raspberry Pi 固件接口（Firmware Interface） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L75) | — | [`raspberrypi,bcm283x-firmware`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/firmware/raspberrypi%2Cbcm283x-firmware.html#std-dtcompatible-raspberrypi-bcm283x-firmware) |
| 通用输入输出与接针（GPIO & Headers） | 片上（on-chip） | BCM2711 通用输入输出（General-Purpose Input/Output，GPIO） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L134) | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L122) | [`brcm,bcm2711-gpio`](../gpio_connectors_bflb_esp_binding_reference/P007_brcm_bcm2711-gpio.md#std-dtcompatible-brcm-bcm2711-gpio) |
| 通用输入输出与接针（GPIO & Headers） | 板上（on-board） | Raspberry Pi BCM283x GPIO 扩展器（GPIO Expander） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L81) | — | [`raspberrypi,bcm283x-gpio`](../gpio_raspberrypi_renesas_binding_reference/P003_raspberrypi_bcm283x-gpio.md#std-dtcompatible-raspberrypi-bcm283x-gpio) |
| 集成电路间总线（Inter-Integrated Circuit，I2C） | 片上（on-chip） | Broadcom BCM2711 I2C 控制器 | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L217) | [5](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L206) | [`brcm,bcm2711-i2c`](../i2c_adi_atmel_esp_binding_reference/P013_brcm_bcm2711-i2c.md#std-dtcompatible-brcm-bcm2711-i2c) |
| 中断控制器（Interrupt Controller） | 片上（on-chip） | ARM 通用中断控制器第2版（Generic Interrupt Controller v2，GICv2） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L89) | — | [`arm,gic-v2`](../interrupt_fabric_binding_reference/P003_arm_gic-v2.md#std-dtcompatible-arm-gic-v2) |
| 发光二极管（Light-Emitting Diode，LED） | 板上（on-board） | 一组由 GPIO 控制的 LED（GPIO-controlled LEDs） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L38) | — | [`gpio-leds`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/gpio-leds.html#std-dtcompatible-gpio-leds) |
| 邮箱（Mailbox） | 片上（on-chip） | Broadcom BCM2711 VideoCore 邮箱（Mailbox） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L104) | — | [`brcm,bcm2711-mbox`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mbox/brcm%2Cbcm2711-mbox.html#std-dtcompatible-brcm-bcm2711-mbox) |
| 引脚控制（Pin Control） | 片上（on-chip） | Broadcom BCM2711 引脚控制器（Pin Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L114) | — | [`brcm,bcm2711-pinctrl`](../pinctrl_adi_ambiq_arm_binding_reference/P017_brcm_bcm2711-pinctrl.md#std-dtcompatible-brcm-bcm2711-pinctrl) |
| 电源域（Power Domain） | 板上（on-board） | Raspberry Pi BCM283x 电源域（Power Domain） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L104) | — | [`raspberrypi,bcm283x-power`](../power_domain_binding_reference/P009_raspberrypi_bcm283x-power.md#std-dtcompatible-raspberrypi-bcm283x-power) |
| 随机数发生器（Random Number Generator，RNG） | 片上（on-chip） | Broadcom iProc RNG200 随机数发生器（Random Number Generator） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L98) | — | [`brcm,iproc-rng200`](../rng_binding_reference/P006_brcm_iproc-rng200.md#std-dtcompatible-brcm-iproc-rng200) |
| 传感器（Sensors） | 板上（on-board） | Raspberry Pi BCM283x 片上系统裸片温度传感器（SoC Die-temperature Sensor） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L88) | — | [`raspberrypi,bcm283x-vc-thermal`](../sensor_realtek_rohm_sensirion_binding_reference/P002_raspberrypi_bcm283x-vc-thermal.md#std-dtcompatible-raspberrypi-bcm283x-vc-thermal) |
| 串行控制器（Serial Controller） | 片上（on-chip） | ARM PL011 通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L146) | [4](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L166) | [`arm,pl011`](../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011) |
| 串行控制器（Serial Controller） | 片上（on-chip） | Broadcom BCM283x 辅助通用异步收发器（Auxiliary UART） | — | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L156) | [`brcm,bcm283x-aux-uart`](../uart_adi_arm_atmel_binding_reference/P014_brcm_bcm283x-aux-uart.md#std-dtcompatible-brcm-bcm283x-aux-uart) |
| 静态随机存取存储器（Static Random-Access Memory，SRAM） | 片上（on-chip） | 通用片上 SRAM（Generic On-chip SRAM） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L83) | — | [`mmio-sram`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sram/mmio-sram.html#std-dtcompatible-mmio-sram) |
| 定时器（Timer） | 片上（on-chip） | 各处理器核心的 ARM 架构定时器（Architected Timer） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L54) | — | [`arm,armv8-timer`](../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer) |
| 通用串行总线（Universal Serial Bus，USB） | 片上（on-chip） | Broadcom BCM2835 USB On-The-Go（OTG）控制器，兼容 DWC2 | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L272) | — | [`brcm,bcm2835-usb`](../usb_controller_binding_reference/P008_brcm_bcm2835-usb.md#std-dtcompatible-brcm-bcm2835-usb) |

<a id="qemu_cortex_a72-qemu_cortex_a72/bcm2711/smp-hw-features-section"></a>

<a id="qemu_cortex_a72-qemu_cortex_a72/bcm2711/smp-hw-features-panel"></a>

<a id="qemu_cortex_a72-qemu_cortex_a72/bcm2711/smp-hw-features-memory"></a>

<a id="qemu_cortex_a72-qemu_cortex_a72/bcm2711/smp-hw-features-table"></a>

### 2.2.2\_目标 `qemu_cortex_a72/bcm2711/smp`

目标存储容量：RAM 为 8 MiB，Flash 为 不适用（N/A）。

| 类型 | 位置 | 说明 | 启用实例 | 禁用实例 | 兼容字符串 |
| --- | --- | --- | ---: | ---: | --- |
| 中央处理器（Central Processing Unit，CPU） | 片上（on-chip） | ARM Cortex-A72 中央处理器（CPU） | [4](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L23) | — | [`arm,cortex-a72`](../cpu_arm_riscv_binding_reference/P012_arm_cortex-a72.md#std-dtcompatible-arm-cortex-a72) |
| 时钟控制（Clock Control） | 片上（on-chip） | 通用固定频率时钟提供者（Generic Fixed-rate Clock Provider） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L67) | — | [`fixed-clock`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/fixed-clock.html#std-dtcompatible-fixed-clock) |
| 显示（Display） | 板上（on-board） | Raspberry Pi BCM2711 帧缓冲显示设备（Framebuffer Display Device） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L94) | — | [`raspberrypi,bcm2711-framebuffer`](../display_panel_renesas_sharp_binding_reference/P006_raspberrypi_bcm2711-framebuffer.md#std-dtcompatible-raspberrypi-bcm2711-framebuffer) |
| 以太网（Ethernet） | 片上（on-chip） | Broadcom GENET 千兆以太网控制器（Gigabit Ethernet Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L293) | — | [`brcm,genet`](../ethernet_mac_mdio_binding_reference/P006_brcm_genet.md#std-dtcompatible-brcm-genet) |
| 以太网（Ethernet） | 片上（on-chip） | Broadcom GENET 管理数据输入输出控制器（Management Data Input/Output，MDIO） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L302) | — | [`brcm,genet-mdio`](../ethernet_mac_mdio_binding_reference/P017_brcm_genet-mdio.md#std-dtcompatible-brcm-genet-mdio) |
| 以太网（Ethernet） | 板上（on-board） | 通用介质无关接口物理层器件（MII PHY） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L152) | — | [`ethernet-phy`](../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| 固件（Firmware） | 板上（on-board） | Raspberry Pi 固件接口（Firmware Interface） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L75) | — | [`raspberrypi,bcm283x-firmware`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/firmware/raspberrypi%2Cbcm283x-firmware.html#std-dtcompatible-raspberrypi-bcm283x-firmware) |
| 通用输入输出与接针（GPIO & Headers） | 片上（on-chip） | BCM2711 通用输入输出（General-Purpose Input/Output，GPIO） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L134) | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L122) | [`brcm,bcm2711-gpio`](../gpio_connectors_bflb_esp_binding_reference/P007_brcm_bcm2711-gpio.md#std-dtcompatible-brcm-bcm2711-gpio) |
| 通用输入输出与接针（GPIO & Headers） | 板上（on-board） | Raspberry Pi BCM283x GPIO 扩展器（GPIO Expander） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L81) | — | [`raspberrypi,bcm283x-gpio`](../gpio_raspberrypi_renesas_binding_reference/P003_raspberrypi_bcm283x-gpio.md#std-dtcompatible-raspberrypi-bcm283x-gpio) |
| 集成电路间总线（Inter-Integrated Circuit，I2C） | 片上（on-chip） | Broadcom BCM2711 I2C 控制器 | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L217) | [5](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L206) | [`brcm,bcm2711-i2c`](../i2c_adi_atmel_esp_binding_reference/P013_brcm_bcm2711-i2c.md#std-dtcompatible-brcm-bcm2711-i2c) |
| 中断控制器（Interrupt Controller） | 片上（on-chip） | ARM 通用中断控制器第2版（Generic Interrupt Controller v2，GICv2） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L89) | — | [`arm,gic-v2`](../interrupt_fabric_binding_reference/P003_arm_gic-v2.md#std-dtcompatible-arm-gic-v2) |
| 发光二极管（Light-Emitting Diode，LED） | 板上（on-board） | 一组由 GPIO 控制的 LED（GPIO-controlled LEDs） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L38) | — | [`gpio-leds`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/gpio-leds.html#std-dtcompatible-gpio-leds) |
| 邮箱（Mailbox） | 片上（on-chip） | Broadcom BCM2711 VideoCore 邮箱（Mailbox） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L104) | — | [`brcm,bcm2711-mbox`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mbox/brcm%2Cbcm2711-mbox.html#std-dtcompatible-brcm-bcm2711-mbox) |
| 引脚控制（Pin Control） | 片上（on-chip） | Broadcom BCM2711 引脚控制器（Pin Controller） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L114) | — | [`brcm,bcm2711-pinctrl`](../pinctrl_adi_ambiq_arm_binding_reference/P017_brcm_bcm2711-pinctrl.md#std-dtcompatible-brcm-bcm2711-pinctrl) |
| 电源域（Power Domain） | 板上（on-board） | Raspberry Pi BCM283x 电源域（Power Domain） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L104) | — | [`raspberrypi,bcm283x-power`](../power_domain_binding_reference/P009_raspberrypi_bcm283x-power.md#std-dtcompatible-raspberrypi-bcm283x-power) |
| 随机数发生器（Random Number Generator，RNG） | 片上（on-chip） | Broadcom iProc RNG200 随机数发生器（Random Number Generator） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L98) | — | [`brcm,iproc-rng200`](../rng_binding_reference/P006_brcm_iproc-rng200.md#std-dtcompatible-brcm-iproc-rng200) |
| 传感器（Sensors） | 板上（on-board） | Raspberry Pi BCM283x 片上系统裸片温度传感器（SoC Die-temperature Sensor） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/raspberrypi/rpi_4b/rpi_4b.dts?plain=1#L88) | — | [`raspberrypi,bcm283x-vc-thermal`](../sensor_realtek_rohm_sensirion_binding_reference/P002_raspberrypi_bcm283x-vc-thermal.md#std-dtcompatible-raspberrypi-bcm283x-vc-thermal) |
| 串行控制器（Serial Controller） | 片上（on-chip） | ARM PL011 通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L146) | [4](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L166) | [`arm,pl011`](../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011) |
| 串行控制器（Serial Controller） | 片上（on-chip） | Broadcom BCM283x 辅助通用异步收发器（Auxiliary UART） | — | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L156) | [`brcm,bcm283x-aux-uart`](../uart_adi_arm_atmel_binding_reference/P014_brcm_bcm283x-aux-uart.md#std-dtcompatible-brcm-bcm283x-aux-uart) |
| 静态随机存取存储器（Static Random-Access Memory，SRAM） | 片上（on-chip） | 通用片上 SRAM（Generic On-chip SRAM） | [2](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L83) | — | [`mmio-sram`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sram/mmio-sram.html#std-dtcompatible-mmio-sram) |
| 定时器（Timer） | 片上（on-chip） | 各处理器核心的 ARM 架构定时器（Architected Timer） | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L54) | — | [`arm,armv8-timer`](../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer) |
| 通用串行总线（Universal Serial Bus，USB） | 片上（on-chip） | Broadcom BCM2835 USB On-The-Go（OTG）控制器，兼容 DWC2 | [1](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/broadcom/bcm2711.dtsi?plain=1#L272) | — | [`brcm,bcm2835-usb`](../usb_controller_binding_reference/P008_brcm_bcm2835-usb.md#std-dtcompatible-brcm-bcm2835-usb) |

<a id="programming-and-debugging"></a>

## 2.3\_编程与调试

`qemu_cortex_a72` 支持以下运行器（Runner）及对应 west 命令：

| 运行器 | `west flash` | `west debug` | `west debugserver` |
| --- | --- | --- | --- |
| `qemu` | 支持，默认 | 支持，默认 | 支持 |

可用此配置在 QEMU 仿真环境中运行基本 Zephyr 应用及内核测试。以下以[基础同步示例（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)为例，从 Zephyr 仓库根目录执行（代码注释 `From the root of the zephyr repository` 也表示这一位置）：

```shell
# From the root of the zephyr repository
west build -b qemu_cortex_a72 samples/synchronization
west build -t run
```

这会构建包含同步示例应用的镜像（Image），使用 QEMU 启动，并显示以下控制台输出（Console Output）：

```text
*** Booting Zephyr OS build v4.4.0-2646-g284aabd6a6c1 ***
thread_a: Hello World from cpu 0 on qemu_cortex_a72!
thread_b: Hello World from cpu 0 on qemu_cortex_a72!
thread_a: Hello World from cpu 0 on qemu_cortex_a72!
thread_b: Hello World from cpu 0 on qemu_cortex_a72!
thread_a: Hello World from cpu 0 on qemu_cortex_a72!
thread_b: Hello World from cpu 0 on qemu_cortex_a72!
thread_a: Hello World from cpu 0 on qemu_cortex_a72!
thread_b: Hello World from cpu 0 on qemu_cortex_a72!
```

按 `CTRL+A`，再按 `x` 退出 QEMU。

> 译注：输出是官方页面给出的示例，版本字符串按原样保留；本次翻译没有运行固件或重新生成这些输出。

<a id="debugging"></a>

### 2.3.1\_调试

详细概述参见[应用调试（Application Debugging）](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

通过 QEMU 的 GDB 调试桩（GDB Stub，以 `-s` 标志启用）连接 GNU 调试器（GDB）：

```shell
gdb-multiarch build/zephyr/zephyr.elf \
  -ex "target remote localhost:1234"
```

<a id="references"></a>

## 2.4\_参考资料

1. [Raspberry Pi 4 Model B 数据手册（Raspberry Pi 4 Model B Datasheet）](https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-datasheet.pdf)。
2. [BCM2711 ARM 外设（BCM2711 ARM Peripherals）](https://datasheets.raspberrypi.com/bcm2711/bcm2711-peripherals.pdf)。

---

[上一章](P001_QEMU_Cortex_A53仿真开发板.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md) · [下一章](P003_QEMU_Cortex_M0仿真开发板.md)
