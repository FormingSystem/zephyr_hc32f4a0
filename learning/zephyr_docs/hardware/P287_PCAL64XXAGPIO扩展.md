---
id: learning.zephyr-docs.hardware.gpioextb-5
title: PCAL64XXAGPIO扩展
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__pcal64xxa__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第287章\_PCAL64XXAGPIO扩展

原文：[group__gpio__pcal64xxa__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__pcal64xxa__interface.html)。读取日期：2026-10-13，`latest`。

## 287.1\_手动复位

NXP PCAL64XXA 是基于集成电路间总线（Inter-Integrated Circuit，I²C）的输入/输出（Input/Output，I/O）扩展器。本页为通用输入/输出（General Purpose Input/Output，GPIO）驱动提供手动复位接口，声明来自 `zephyr/drivers/gpio/gpio_pcal64xxa.h`。

函数 [`pcal64xxa_reset()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__pcal64xxa__interface.html#ga43c22f38602347e2e95f63fd9b31dc96) 手动复位PCAL64XXA：

```c
int pcal64xxa_reset(const struct device *dev);
```

默认已启用自动复位（Automatic Reset）；只有禁用了自动复位后，才需要手动复位。`dev` 指向驱动实例的设备结构。成功返回 `0`，原页没有列出其他返回码。

---

[上一章：PCAGPIO扩展](P286_PCAGPIO扩展.md) · [下一章：SX1509BGPIO扩展](P288_SX1509BGPIO扩展.md) · [返回大纲](大纲.md)
