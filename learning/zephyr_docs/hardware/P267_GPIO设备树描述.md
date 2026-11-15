---
id: learning.zephyr-docs.hardware.gpiostruct-0
title: GPIO设备树描述
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgpio__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第267章\_GPIO设备树描述

原文：[structgpio__dt__spec](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__dt__spec.html)。读取日期：2026-10-13，`latest`。

## 267.1\_用途与成员

结构 [`gpio_dt_spec`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__dt__spec.html) 保存 **设备树（Devicetree）**中指定的 **通用输入/输出（General Purpose Input/Output，GPIO）**引脚信息，声明来自 `zephyr/drivers/gpio.h`。

它包含控制器设备指针、该设备控制的引脚编号，以及可以在设备树中给出的那部分引脚配置标志。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="a5d617d47e2f568c7a4402a8f5a40ed4f"></a>[`port`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__dt__spec.html#a5d617d47e2f568c7a4402a8f5a40ed4f) | `const struct device *` | 控制该引脚的GPIO设备 |
| <a id="ad7e6fbb0cba0be94a47d4f2add056c84"></a>[`pin`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__dt__spec.html#ad7e6fbb0cba0be94a47d4f2add056c84) | [`gpio_pin_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga38179eb7a46a743c12cfac28f347fb34) | 引脚在该设备上的编号 |
| <a id="ae3b90e7e22708798c67da94f72ad1ab0"></a>[`dt_flags`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__dt__spec.html#ae3b90e7e22708798c67da94f72ad1ab0) | [`gpio_dt_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gad435719dccdc37c05852960a7218fbd2) | 设备树中指定的引脚配置标志 |

## 267.2\_相关初始化宏

相关宏均返回静态初始化器（Static Initializer）：[`GPIO_DT_SPEC_GET_BY_IDX`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gacb1077b77aecf8f1a9c7636ea583c4cf) 按索引取得描述，[`GPIO_DT_SPEC_GET_BY_IDX_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga3db4fa464e191016287f4c4d7eb9a983) 提供回退值，[`GPIO_DT_SPEC_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga2fa6bb5880f46984f9fc29c70f7d503e) 读取索引0，[`GPIO_DT_SPEC_GET_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga26b2205aa82819df1d80a22761352e71) 为索引0提供回退。完整参数和规则见[GPIO公共接口](P266_GPIO公共接口.md)。

---

[上一章：GPIO公共接口](P266_GPIO公共接口.md) · [下一章：GPIO公共驱动配置](P268_GPIO公共驱动配置.md) · [返回大纲](大纲.md)
