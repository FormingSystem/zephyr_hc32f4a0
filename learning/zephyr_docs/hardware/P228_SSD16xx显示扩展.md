---
id: learning.zephyr-docs.hardware.dispext-5
title: SSD16xx显示扩展
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ssd16xx__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第228章\_SSD16xx显示扩展

原文：[group__ssd16xx__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__ssd16xx__interface.html)。读取日期：2026-10-13，`latest`。

## 228.1\_范围与头文件

本页提供 Solomon SSD16xx **电泳显示器（Electrophoretic Display，EPD）**控制器的扩展 **应用程序编程接口（Application Programming Interface，API）**，声明来自官方头文件 `zephyr/display/ssd16xx.h`。

## 228.2\_内部缓冲区类型

枚举 [`ssd16xx_ram`](https://docs.zephyrproject.org/latest/doxygen/html/group__ssd16xx__interface.html#gaf3596acb60f20fbecef01e82672ea765) 选择直接访问的 **随机存取存储器（Random Access Memory，RAM）**类型：

| 枚举项 | 含义 |
| --- | --- |
| `SSD16XX_RAM_BLACK = 0` | 黑色 RAM 缓冲区，通常用于组织下一次刷新后要显示的内容。 |
| [`SSD16XX_RAM_RED`](https://docs.zephyrproject.org/latest/doxygen/html/group__ssd16xx__interface.html#ggaf3596acb60f20fbecef01e82672ea765a54fddbd6e9f2207ff228ccfcde65f466) | 红色 RAM 缓冲区，通常在局部刷新（Partial Refresh）时作为旧帧缓冲区，或作为额外的颜色通道。 |

## 228.3\_直接读取RAM

函数 [`ssd16xx_read_ram()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ssd16xx__interface.html#ga876bae07401b2ccc3889414706ae4d97) 直接读取 SSD16xx 控制器内部 RAM：

```c
int ssd16xx_read_ram(const struct device *dev, enum ssd16xx_ram ram_type,
    const uint16_t x, const uint16_t y,
    const struct display_buffer_descriptor *desc, void *buf);
```

| 参数 | 含义 |
| --- | --- |
| `dev` | 指向设备结构。 |
| `ram_type` | 要读取的 RAM 类型。 |
| `x`、`y` | 相对于左上角的坐标。 |
| `desc` | 描述缓冲区布局的结构，见[显示缓冲区描述符](P215_显示缓冲区描述符.md)。 |
| `buf` | 输出缓冲区。 |

成功返回 0，失败返回负的错误码（Negative errno Code）。

---

[上一章：设备树显示接口](P227_设备树显示接口.md) · [下一章：步进电机接口目录](P229_步进电机接口目录.md) · [返回大纲](大纲.md)
