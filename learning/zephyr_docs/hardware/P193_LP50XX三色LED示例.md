---
id: learning.zephyr-docs.hardware.lpsamp-1
title: LP50XX三色LED示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/led/lp50xx/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="lp50xx"></a>

# 第193章\_LP50XX三色LED示例

原文：[LP50XX RGB LED](https://docs.zephyrproject.org/latest/samples/drivers/led/lp50xx/README.html)。读取日期：2026-10-13，`latest`。

## 193.1\_概述（Overview）

本示例控制接在 LP50xx 驱动器上的最多 12 个 **发光二极管（Light-Emitting Diode，LED）**，其颜色由红、绿、蓝（Red, Green, Blue，RGB）分量构成。

首先通过 `led_get_info()` **系统调用（System Call）**取得每个 LED 的信息，并打印到日志中。之后进入无限循环：先用 [`led_write_channels()`](P202_LED公共接口.md) 系统调用对全部 LED 同时执行下述图案，再用 [`led_set_brightness()`](P202_LED公共接口.md) 和 [`led_set_color()`](P202_LED公共接口.md) 系统调用对各灯逐个执行。

## 193.2\_测试图案（Test Pattern）

先通过通道 **应用程序编程接口（Application Programming Interface，API）**控制所有 LED，再逐个控制每个 LED。每一轮都依次使用红、绿、蓝、白、黄、紫、青、橙八种颜色，并针对每种颜色执行：

1. 设置颜色。
2. 点亮。
3. 关闭。
4. 逐渐把亮度增大到最大值。
5. 关闭。

## 193.3\_构建与运行（Building and Running）

开发板需要通过 **内部集成电路总线（Inter-Integrated Circuit，I2C）**连接 LP5009、LP5012、LP5018、LP5024、LP5030 或 LP5036 驱动器，并在开发板的 **设备树源（Devicetree Source，DTS）**文件中定义与相应器件绑定（Binding）匹配的节点。

官方提供 [LPCXpresso11U68](https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso11u68/doc/index.html#lpcxpresso11u68) 的叠加文件 `boards/lpcxpresso11u68.overlay`，路径相对于示例目录。它假定一个接有 10 个 LED 的 LP5030 驱动器连接到 I2C0，总线地址为 `0x30`。

## 193.4\_参考资料（References）

- [LP5009/LP5012数据手册](https://www.ti.com/lit/ds/symlink/lp5012.pdf)。
- [LP5018/LP5024数据手册](https://www.ti.com/lit/ds/symlink/lp5024.pdf)。
- [LP5030/LP5036数据手册](https://www.ti.com/lit/ds/symlink/lp5036.pdf)。

[LED接口](P202_LED公共接口.md) · [官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/led/lp50xx)

[上一章：LP3943四色LED示例](P192_LP3943四色LED示例.md) · [下一章：LP5562三色LED示例](P194_LP5562三色LED示例.md) · [返回大纲](大纲.md)
