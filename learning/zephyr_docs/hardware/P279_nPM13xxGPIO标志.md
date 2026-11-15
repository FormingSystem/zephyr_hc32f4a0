---
id: learning.zephyr-docs.hardware.gpioext-5
title: nPM13xxGPIO标志
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第279章\_nPM13xxGPIO标志

原文：[group__gpio__interface__npm13xx](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html)。读取日期：2026-10-13，`latest`。

## 279.1\_标志编码

本页定义 nPM13xx 的通用输入/输出（General Purpose Input/Output，GPIO）专用标志，声明来自 `zephyr/dt-bindings/gpio/nordic-npm13xx-gpio.h`。

标志编码在设备树（Devicetree）GPIO类型 [`gpio_dt_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gad435719dccdc37c05852960a7218fbd2) 的高8位：第8位选择驱动强度（Drive Strength），0为1 mA、1为6 mA；第9位控制去抖（Debounce），第10位控制看门狗复位（Watchdog Reset），第11位控制掉电警告（Power Loss Warning），后三位均为0关闭、1开启。

## 279.2\_宏定义

| 宏 | 原定义 | 含义 |
| --- | --- | --- |
| [`NPM13XX_GPIO_DRIVE_1MA`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga6a747e318dbdecb394e6c97055cf7d3b) | `(0U << 8U)` | 1 mA驱动 |
| [`NPM13XX_GPIO_DRIVE_6MA`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga29c65d6c81acd6c6474a8d5463d30312) | `(1U << 8U)` | 6 mA驱动 |
| [`NPM13XX_GPIO_DEBOUNCE_OFF`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga94b628f01bd35ef5a8c4be5810853d8a) | `(0U << 9U)` | 去抖关闭；原单项说明为“正常驱动” |
| [`NPM13XX_GPIO_DEBOUNCE_ON`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga37203fc635db945392c25ba5eddb42ad) | `(1U << 9U)` | 去抖开启；原单项说明为“高驱动” |
| [`NPM13XX_GPIO_WDT_RESET_OFF`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga7e835aa905fce6b9bd88f6c113ad8fbd) | `(0U << 10U)` | 关闭看门狗复位 |
| [`NPM13XX_GPIO_WDT_RESET_ON`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#gac17073bd2d8bda878c0cf7307276efcb) | `(1U << 10U)` | 开启看门狗复位 |
| [`NPM13XX_GPIO_PWRLOSSWARN_OFF`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#ga8aa4cab9a6961ca60a14e1cae448376e) | `(0U << 11U)` | 关闭掉电警告 |
| [`NPM13XX_GPIO_PWRLOSSWARN_ON`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm13xx.html#gae774196d9a4258da3d849899de5b744b) | `(1U << 11U)` | 开启掉电警告 |

> 译注：去抖宏的单项文字说明在原文中写成“Normal drive / High drive”，与宏名和第9位的整体说明不一致。表中保留原单项说明，并依据同页位定义标明去抖开关含义。

---

[上一章：nPM10xxGPIO标志](P278_nPM10xxGPIO标志.md) · [下一章：nPM2100GPIO标志](P280_nPM2100GPIO标志.md) · [返回大纲](大纲.md)
