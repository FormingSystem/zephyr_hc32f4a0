---
id: learning.zephyr-docs.api-directory-indices.page-272
title: interrupt-controller目录参考（Directory Reference）
kind: reference
status: maintained
domains: [zephyr, documentation, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dir_f11fd9ad294c5739f2cbe07a93c59a1b.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；章节编号和导航为本地新增。 -->

# 第272章\_interrupt-controller目录参考（Directory Reference）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dir_f11fd9ad294c5739f2cbe07a93c59a1b.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

官方目录层次：`zephyr/dt-bindings/interrupt-controller`。

条目说明采用中文译文并附英文原文，便于核对术语与接口；文件名、类型名和符号保持原样。目录树已完整展开，原页的折叠控件不参与本地静态阅读。

<div>
<table>
<tr><td colspan="2"><h2><a id="header-files"></a><span data-translation="0">文件（Files）。</span><br><small lang="en" data-source-prose="0"><a id="files"></a>
Files</small></h2>
</td></tr>

<tr><td><a id="r_arm-gic_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/arm-gic_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/arm-gic_8h.html">arm-gic.h</a></td></tr>

<tr><td> </td><td><span data-translation="1">Arm通用中断控制器（GIC）的设备树宏。</span><br><small lang="en" data-source-prose="1">Arm GIC interrupt controller devicetree macros. <br></small></td></tr>

<tr><td><a id="r_bcm2835-armctrl_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/bcm2835-armctrl_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/bcm2835-armctrl_8h.html">bcm2835-armctrl.h</a></td></tr>

<tr><td> </td><td><span data-translation="2">BCM2835 ARMC外设中断控制器的设备树中断号（IRQ Number）绑定，涉及组0至2；原摘要在“see datasheet ch.”处结束，未给出数据手册章节号。</span><br><small lang="en" data-source-prose="2">Devicetree IRQ-number bindings for the BCM2835 ARMC peripheral interrupt controller (banks 0..2; see datasheet ch. <br></small></td></tr>

<tr><td><a id="r_bcm2836-l1_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/bcm2836-l1_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/bcm2836-l1_8h.html">bcm2836-l1.h</a></td></tr>

<tr><td> </td><td><span data-translation="3">BCM2836 ARM本地中断控制器（ARM-Local Interrupt Controller）的设备树中断号绑定，包括每核定时器、邮箱、GPU级联和PMU中断源。</span><br><small lang="en" data-source-prose="3">Devicetree IRQ-number bindings for the BCM2836 ARM-local interrupt controller (per-core timers, mailboxes, GPU cascade and PMU sources). <br></small></td></tr>

<tr><td><a id="r_esp-esp32c2-intmux_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32c2-intmux_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32c2-intmux_8h.html">esp-esp32c2-intmux.h</a></td></tr>

<tr><td> </td><td><span data-translation="4">Espressif ESP32-C2用于设备树的中断源定义（Interrupt Source Definitions）。</span><br><small lang="en" data-source-prose="4">Espressif ESP32-C2 interrupt source definitions for devicetree. <br></small></td></tr>

<tr><td><a id="r_esp-esp32c3-intmux_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32c3-intmux_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32c3-intmux_8h.html">esp-esp32c3-intmux.h</a></td></tr>

<tr><td> </td><td><span data-translation="5">Espressif ESP32-C3用于设备树的中断源定义（Interrupt Source Definitions）。</span><br><small lang="en" data-source-prose="5">Espressif ESP32-C3 interrupt source definitions for devicetree. <br></small></td></tr>

<tr><td><a id="r_esp-esp32c5-intmux_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32c5-intmux_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32c5-intmux_8h.html">esp-esp32c5-intmux.h</a></td></tr>

<tr><td> </td><td><span data-translation="6">ESP32-C5用于设备树绑定的中断多路复用器定义（Interrupt Multiplexer Definitions）。</span><br><small lang="en" data-source-prose="6">ESP32-C5 interrupt multiplexer definitions for device tree bindings. <br></small></td></tr>

<tr><td><a id="r_esp-esp32c6-intmux_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32c6-intmux_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32c6-intmux_8h.html">esp-esp32c6-intmux.h</a></td></tr>

<tr><td> </td><td><span data-translation="7">Espressif ESP32-C6用于设备树的中断源定义（Interrupt Source Definitions）。</span><br><small lang="en" data-source-prose="7">Espressif ESP32-C6 interrupt source definitions for devicetree. <br></small></td></tr>

<tr><td><a id="r_esp-esp32c61-intmux_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32c61-intmux_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32c61-intmux_8h.html">esp-esp32c61-intmux.h</a></td></tr>

<tr><td> </td><td><span data-translation="8">ESP32-C61用于设备树绑定的中断多路复用器定义（Interrupt Multiplexer Definitions）。</span><br><small lang="en" data-source-prose="8">ESP32-C61 interrupt multiplexer definitions for device tree bindings. <br></small></td></tr>

<tr><td><a id="r_esp-esp32h2-intmux_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32h2-intmux_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32h2-intmux_8h.html">esp-esp32h2-intmux.h</a></td></tr>

<tr><td> </td><td><span data-translation="9">Espressif ESP32-H2用于设备树的中断源定义（Interrupt Source Definitions）。</span><br><small lang="en" data-source-prose="9">Espressif ESP32-H2 interrupt source definitions for devicetree. <br></small></td></tr>

<tr><td><a id="r_esp-esp32p4-intmux_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32p4-intmux_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp-esp32p4-intmux_8h.html">esp-esp32p4-intmux.h</a></td></tr>

<tr><td> </td><td><span data-translation="10">Espressif ESP32-P4的中断源定义（Interrupt Source Definitions）。</span><br><small lang="en" data-source-prose="10">Interrupt source definitions for Espressif ESP32-P4. <br></small></td></tr>

<tr><td><a id="r_esp-xtensa-intmux_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp-xtensa-intmux_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp-xtensa-intmux_8h.html">esp-xtensa-intmux.h</a></td></tr>

<tr><td> </td><td><span data-translation="11">Espressif ESP32用于设备树的中断源定义（Interrupt Source Definitions）。</span><br><small lang="en" data-source-prose="11">Espressif ESP32 interrupt source definitions for devicetree. <br></small></td></tr>

<tr><td><a id="r_esp32s2-xtensa-intmux_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp32s2-xtensa-intmux_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp32s2-xtensa-intmux_8h.html">esp32s2-xtensa-intmux.h</a></td></tr>

<tr><td> </td><td><span data-translation="12">Espressif ESP32-S2用于设备树的中断源定义（Interrupt Source Definitions）。</span><br><small lang="en" data-source-prose="12">Espressif ESP32-S2 interrupt source definitions for devicetree. <br></small></td></tr>

<tr><td><a id="r_esp32s3-xtensa-intmux_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp32s3-xtensa-intmux_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/esp32s3-xtensa-intmux_8h.html">esp32s3-xtensa-intmux.h</a></td></tr>

<tr><td> </td><td><span data-translation="13">Espressif ESP32-S3用于设备树的中断源定义（Interrupt Source Definitions）。</span><br><small lang="en" data-source-prose="13">Espressif ESP32-S3 interrupt source definitions for devicetree. <br></small></td></tr>

<tr><td><a id="r_infineon-xmc4xxx-intc_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/infineon-xmc4xxx-intc_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/infineon-xmc4xxx-intc_8h.html">infineon-xmc4xxx-intc.h</a></td></tr>

<tr><td> </td><td><span data-translation="14">Infineon XMC4xxx中断控制器（Interrupt Controller）的设备树宏。</span><br><small lang="en" data-source-prose="14">Infineon XMC4xxx interrupt controller devicetree macros. <br></small></td></tr>

<tr><td><a id="r_intel-ioapic_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/intel-ioapic_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/intel-ioapic_8h.html">intel-ioapic.h</a></td></tr>

<tr><td> </td><td><span data-translation="15">Intel输入输出高级可编程中断控制器（I/O APIC）的设备树宏。</span><br><small lang="en" data-source-prose="15">Intel I/O APIC interrupt controller devicetree macros. <br></small></td></tr>

<tr><td><a id="r_it8xxx2-wuc_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2-wuc_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2-wuc_8h.html">it8xxx2-wuc.h</a></td></tr>

<tr><td> </td><td><span data-translation="16">ITE IT8XXX2唤醒控制器（Wake-Up Controller）的设备树宏。</span><br><small lang="en" data-source-prose="16">ITE IT8XXX2 wake-up controller devicetree macros. <br></small></td></tr>

<tr><td><a id="r_ite-intc_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/ite-intc_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/ite-intc_8h.html">ite-intc.h</a></td></tr>

<tr><td> </td><td><span data-translation="17">ITE IT8XXX2中断控制器（Interrupt Controller）的设备树宏。</span><br><small lang="en" data-source-prose="17">ITE IT8XXX2 interrupt controller devicetree macros. <br></small></td></tr>

<tr><td><a id="r_ite-it51xxx-intc_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/ite-it51xxx-intc_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/ite-it51xxx-intc_8h.html">ite-it51xxx-intc.h</a></td></tr>

<tr><td> </td><td><span data-translation="18">ITE IT51XXX中断控制器（Interrupt Controller）的设备树宏。</span><br><small lang="en" data-source-prose="18">ITE IT51XXX interrupt controller devicetree macros. <br></small></td></tr>

<tr><td><a id="r_ite-it51xxx-wuc_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/ite-it51xxx-wuc_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/ite-it51xxx-wuc_8h.html">ite-it51xxx-wuc.h</a></td></tr>

<tr><td> </td><td><span data-translation="19">ITE IT51XXX唤醒控制器（Wake-Up Controller）的设备树宏。</span><br><small lang="en" data-source-prose="19">ITE IT51XXX wake-up controller devicetree macros. <br></small></td></tr>

<tr><td><a id="r_mchp-xec-ecia_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-ecia_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-ecia_8h.html">mchp-xec-ecia.h</a></td></tr>

<tr><td> </td><td><span data-translation="20">Microchip XEC嵌入式控制器中断聚合器（ECIA）的设备树宏。</span><br><small lang="en" data-source-prose="20">Microchip XEC ECIA interrupt controller devicetree macros. <br></small></td></tr>

<tr><td><a id="r_microchip-smartfusion2-irq_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/microchip-smartfusion2-irq_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/microchip-smartfusion2-irq_8h.html">microchip-smartfusion2-irq.h</a></td></tr>

<tr><td> </td><td><span data-translation="21">Microchip SmartFusion2中断控制器（Interrupt Controller）的设备树宏。</span><br><small lang="en" data-source-prose="21">Microchip SmartFusion2 interrupt controller devicetree macros. <br></small></td></tr>

<tr><td><a id="r_openisa-intmux_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/openisa-intmux_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/openisa-intmux_8h.html">openisa-intmux.h</a></td></tr>

<tr><td> </td><td><span data-translation="22">OpenISA RV32M1中断多路复用器（INTMUX）的设备树宏。</span><br><small lang="en" data-source-prose="22">OpenISA RV32M1 INTMUX devicetree macros. <br></small></td></tr>

<tr><td><a id="r_rts5817_5Fintc_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/rts5817__intc_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/rts5817__intc_8h.html">rts5817_intc.h</a></td></tr>

<tr><td> </td><td><span data-translation="23">Realtek RTS5817的中断源编号（Interrupt Source Numbers）。</span><br><small lang="en" data-source-prose="23">Realtek RTS5817 interrupt source numbers. <br></small></td></tr>

<tr><td><a id="r_ti-vim_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/ti-vim_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/ti-vim_8h.html">ti-vim.h</a></td></tr>

<tr><td> </td><td><span data-translation="24">TI向量中断管理器（VIM）的设备树宏。</span><br><small lang="en" data-source-prose="24">TI VIM interrupt controller devicetree macros. <br></small></td></tr>

</table>

</div>


---

[上一章](P271_debug_f1105249_目录.md) · [返回大纲](大纲.md) · [下一章](P273_acpi_f2ded791_目录.md)
