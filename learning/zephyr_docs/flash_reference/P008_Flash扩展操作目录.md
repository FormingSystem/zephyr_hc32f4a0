---
id: learning.zephyr-docs.flash-reference.page-8
title: Flash扩展操作目录
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__flash__ex__op.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_Flash扩展操作目录

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__ex__op.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是闪存（Flash）应用程序接口（Application Programming Interface，API）参考。先读[Flash概述](../hardware/P012_Flash闪存.md)理解设备偏移，再按[本册大纲](大纲.md)区分应用接口、驱动后端（Driver Backend）、页布局（Page Layout）和扩展操作。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

闪存驱动的厂商专用扩展操作（Vendor-specific Extended Operations）。

<a id="details"></a>

闪存驱动的厂商专用扩展操作（Vendor-specific Extended Operations）。

<a id="header-groups"></a>
<a id="groups"></a>

## 8.1\_主题（Topics）

<a id="r_andes_5Fflash_5Fxip_5Fex_5Fop"></a>

相关声明：[Andes QSPI-NOR 就地执行（XIP）](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html)。

Andes QSPI-NOR 就地执行（Execute In Place，XIP）闪存的扩展操作。

<a id="r_it51xxx_5Fflash_5Fex_5Fop"></a>

相关声明：[IT51XXX](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html)。

IT51XXX 闪存控制器的扩展操作。

<a id="r_mchp_5Fflash_5Finterface"></a>

相关声明：[Microchip](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html)。

Microchip G3 闪存控制器的扩展操作。

<a id="r_mchp_5Fnvmctrl_5Fg1_5Fflash_5Fex_5Fop"></a>

相关声明：[Microchip NVMCTRL G1](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html)。

Microchip NVMCTRL G1 闪存控制器的扩展操作。

<a id="r_npcx_5Fflash_5Fex_5Fop"></a>

相关声明：[NPCX](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html)。

NPCX 闪存控制器的扩展操作。

<a id="r_rts5912_5Fflash_5Fex_5Fop"></a>

相关声明：[Realtek RTS5912](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html)。

Realtek RTS5912 闪存控制器的扩展操作。

<a id="r_ra_5Fflash_5Fex_5Fop"></a>

相关声明：[Renesas RA](https://docs.zephyrproject.org/latest/doxygen/html/group__ra__flash__ex__op.html)。

Renesas RA 闪存控制器的扩展操作。

<a id="r_m95p32_5Fflash_5Fex_5Fop"></a>

相关声明：[ST M95P32](P011_M95P32扩展操作接口.md)。

ST M95P32 页式电可擦可编程只读存储器（Electrically Erasable Programmable Read-only Memory，EEPROM）的扩展操作。

<a id="r_stm32_5Fflash_5Fex_5Fop"></a>

相关声明：[STM32](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html)。

STM32 闪存控制器的扩展操作。

## 8.2\_源码定位与版本边界

这些接口定义在 [flash.h](../../../include/zephyr/drivers/flash.h)，辅助操作与页遍历分别见 [flash_util.c](../../../drivers/flash/flash_util.c) 和 [flash_page_layout.c](../../../drivers/flash/flash_page_layout.c)。仓库相对链接供跟踪，不能自动视为与网页同版本。译注核对了本次读取的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/flash.h)、[辅助实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_util.c)与[页布局实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_page_layout.c)，三份源码摘要单独记录；main 和 latest 都会滚动更新。本批只翻译和核对源码，没有构建、擦写存储或实板验证。

> 译注——范围：以上为官方扩展操作分组，目录译完不表示每个厂商扩展 API 已译完。对应页面仍按全站清单单独跟踪；这些分组不构成本项目新增芯片资料。

## 8.3\_原页交叉引用（Cross References）

- [Andes QSPI-NOR 就地执行（XIP）](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html)
- [IT51XXX](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html)
- [Microchip](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html)
- [Microchip NVMCTRL G1](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html)
- [NPCX](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html)
- [Realtek RTS5912](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html)
- [Renesas RA](https://docs.zephyrproject.org/latest/doxygen/html/group__ra__flash__ex__op.html)
- [ST M95P32](P011_M95P32扩展操作接口.md)
- [STM32](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html)

<a id="header-details"></a>

---

[上一章](P007_Flash驱动操作结构.md) · [返回大纲](大纲.md) · [下一章](P009_Flash公共头文件参考.md)
