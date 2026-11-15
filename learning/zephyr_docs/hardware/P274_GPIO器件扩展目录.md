---
id: learning.zephyr-docs.hardware.gpioext-0
title: GPIO器件扩展目录
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__ext.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第274章\_GPIO器件扩展目录

原文：[group__gpio__interface__ext](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__ext.html)。读取日期：2026-10-13，`latest`。

## 274.1\_扩展分组

本页汇总通用输入/输出（General Purpose Input/Output，GPIO）的器件专用接口。表中的厂商与器件名称保留原名；集成电路间总线（Inter-Integrated Circuit，I²C）表示扩展器所用总线。

| 分组 | 说明 |
| --- | --- |
| [Ambiq](P282_AmbiqGPIO扩展.md) | Ambiq GPIO控制器 |
| [Bouffalolab BL61x](P283_BL61xGPIO线输出.md) | GPIO先进先出队列（First In, First Out，FIFO）/线输出（Wire Out）接口 |
| [MAX32](P277_MAX32GPIO标志.md) | MAX32专用标志 |
| [NCT38XX](P285_NCT38XXGPIO扩展.md) | Nuvoton NCT38XX系列I²C GPIO扩展器 |
| [NXP MCUX LPC](P284_LPCGPIO扩展.md) | NXP MCUX LPC GPIO控制器 |
| [NXP PCA系列](P286_PCAGPIO扩展.md) | 基于I²C的输入/输出（Input/Output，I/O）扩展器 |
| [NXP PCAL64XXA](P287_PCAL64XXAGPIO扩展.md) | 基于I²C的I/O扩展器 |
| [STM32](P275_STM32GPIO标志.md) | STM32专用标志 |
| [SX1509B](P288_SX1509BGPIO扩展.md) | Semtech SX1509B低电压、电平转换（Level-shifting）GPIO控制器 |
| [nPM10xx](P278_nPM10xxGPIO标志.md) | 标志编码在 [`gpio_dt_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gad435719dccdc37c05852960a7218fbd2) 的高8位 |
| [nPM13xx](P279_nPM13xxGPIO标志.md) | nPM13xx专用标志 |
| [nPM2100](P280_nPM2100GPIO标志.md) | nPM2100专用标志 |
| [nPM6001](P281_nPM6001GPIO标志.md) | nPM6001专用标志 |
| [nRF](P276_nRFGPIO标志.md) | nRF专用标志 |

---

[上一章：GPIO模拟接口](P273_GPIO模拟接口.md) · [下一章：STM32GPIO标志](P275_STM32GPIO标志.md) · [返回大纲](大纲.md)
