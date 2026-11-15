---
id: learning.zephyr-docs.hardware.pwmext-4
title: WisBlockPWM通道
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-pwm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第265章\_WisBlockPWM通道

原文：[group__wisblock-pwm](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-pwm.html)。读取日期：2026-10-13，官方 `latest` 文档版本。

## 265.1\_连接器通道常量

本页定义 WisBlock 连接器暴露的 **脉宽调制（Pulse Width Modulation，PWM）**通道常量。声明文件为 `zephyr/dt-bindings/pwm/wisblock-pwm.h`。

连接器上的输入/输出（Input/Output，IO）端依次命名为 IO1 至 IO7。下表列出对应通道宏及其编号。

| 宏 | 数值 | 对应 IO 端 |
| --- | --- | --- |
| [`WISBLOCK_PWM_IO1`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-pwm.html#gabacaaecb95b9a9993747a6b69025feab) | `0` | IO1 的 PWM 通道 |
| [`WISBLOCK_PWM_IO2`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-pwm.html#ga543fc8ae40ae74c070d8d4e8445a7d7b) | `1` | IO2 的 PWM 通道 |
| [`WISBLOCK_PWM_IO3`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-pwm.html#gaf3280465c864eea8f05530484f301887) | `2` | IO3 的 PWM 通道 |
| [`WISBLOCK_PWM_IO4`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-pwm.html#ga130d25d8ef5aa664acbd9c6830bc030f) | `3` | IO4 的 PWM 通道 |
| [`WISBLOCK_PWM_IO5`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-pwm.html#ga9504f608d22a7a5d24f873229d10f4ac) | `4` | IO5 的 PWM 通道 |
| [`WISBLOCK_PWM_IO6`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-pwm.html#ga41fcb9ec7f8d97b3d66c75e63be5df43) | `5` | IO6 的 PWM 通道 |
| [`WISBLOCK_PWM_IO7`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-pwm.html#ga4075b25c75a5b79e5e99713d8eacf232) | `6` | IO7 的 PWM 通道 |

---

[上一章：设备树PWM宏](P264_设备树PWM宏.md) · [下一章：GPIO公共接口](P266_GPIO公共接口.md) · [返回大纲](大纲.md)
