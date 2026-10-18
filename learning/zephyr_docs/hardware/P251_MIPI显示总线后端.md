---
id: learning.zephyr-docs.hardware.mipibackend-0
title: MIPI显示总线后端
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第251章\_MIPI显示总线后端

原文：[group__mipi__dbi__interface__backend](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html)。读取日期：2026-10-13，`latest`。

## 251.1\_用途

本组提供实现 MIPI **显示总线接口（Display Bus Interface，DBI）**驱动所需的 **应用程序编程接口（Application Programming Interface，API）**类型、回调签名（Callback Signature）及辅助内容，声明来自 `zephyr/drivers/mipi_dbi.h`。

驱动操作由[函数表](P252_MIPI显示总线函数表.md)提供，参数语义见[公共接口](P245_MIPI显示总线接口.md)。

配置参数使用[DBI配置结构](P247_MIPI显示总线配置.md)。TE 为撕裂效应同步信号（Tearing Effect）；复位及 TE 回调中的 [`k_timeout_t`](../timer_reference/P087_内核超时类型.md) 是内核超时类型（Kernel Timeout Type）。

## 251.2\_回调类型

以下为函数指针类型定义（Function Pointer Typedef）。

**类型 [`mipi_dbi_command_write_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga3ea6251e2fe3a18c8daba66c4ded41d6)：向显示控制器写入命令。** 参数说明见函数 [`mipi_dbi_command_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gad36e3d57fd931236c4ed4e58dfef1cca)。

```c
typedef int(* mipi_dbi_command_write_t) (const struct device *dev, const struct mipi_dbi_config *config, uint8_t cmd, const uint8_t *data, size_t len);
```

**类型 [`mipi_dbi_command_read_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga7c6f09c6fece9c343aa4717150ca170e)：读取显示控制器的命令响应。** 参数说明见函数 [`mipi_dbi_command_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gafac64feca9fdee3803154bacb58e8e47)。

```c
typedef int(* mipi_dbi_command_read_t) (const struct device *dev, const struct mipi_dbi_config *config, uint8_t *cmds, size_t num_cmds, uint8_t *response, size_t len);
```

**类型 [`mipi_dbi_write_display_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#gad973c1d30050ea3b6c3f9e1032e5383c)：向显示控制器写入显示缓冲区。** 参数说明见函数 [`mipi_dbi_write_display()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga62aa7b9677da010a678580d956f7d0e3)。

```c
typedef int(* mipi_dbi_write_display_t) (const struct device *dev, const struct mipi_dbi_config *config, const uint8_t *framebuf, struct display_buffer_descriptor *desc, enum display_pixel_format pixfmt);
```

**类型 [`mipi_dbi_reset_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga37ac264a3130d34a8d594c7482b09870)：复位所连接的显示控制器。** 参数说明见函数 [`mipi_dbi_reset()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#ga1c1a117ae5db5f7508f302d48dc72013)。

```c
typedef int(* mipi_dbi_reset_t) (const struct device *dev, k_timeout_t delay);
```

**类型 [`mipi_dbi_release_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga12f0446626ab4feb996f33fcea4129dd)：释放锁定的 DBI 设备。** 参数说明见函数 [`mipi_dbi_release()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gade0b635bcd4f16fb3ec5d122d1b09161)。

```c
typedef int(* mipi_dbi_release_t) (const struct device *dev, const struct mipi_dbi_config *config);
```

**类型 [`mipi_dbi_configure_te_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga2000c1dc2ac1efe0eb6179a18da1e5c2)：配置撕裂效应同步信号。** 参数说明见函数 [`mipi_dbi_configure_te()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface.html#gab74f96d99f9702f29b51cc2fe0b48d95)。

```c
typedef int(* mipi_dbi_configure_te_t) (const struct device *dev, uint8_t edge, k_timeout_t delay);
```

> 译注：复位和 TE 配置的后端参数类型为 `k_timeout_t delay`；公共函数分别使用毫秒整数 `delay_ms` 和微秒整数 `delay_us`。这里保留各自声明，不把它们当作同一种函数指针类型。

---

[上一章：MIPI显示串行消息](P250_MIPI显示串行消息.md) · [下一章：MIPI显示总线函数表](P252_MIPI显示总线函数表.md) · [返回大纲](大纲.md)
