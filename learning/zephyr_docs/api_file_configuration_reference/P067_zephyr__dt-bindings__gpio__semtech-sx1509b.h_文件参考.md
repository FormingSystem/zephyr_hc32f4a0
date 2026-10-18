---
id: learning.zephyr-docs.api-file-configuration-reference.page-67
title: zephyr__dt-bindings__gpio__semtech-sx1509b.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/semtech-sx1509b_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_zephyr\_\_dt-bindings\_\_gpio\_\_semtech-sx1509b.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/semtech-sx1509b_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 67.1\_宏定义（Macros）

<a id="r_a319917ebc030e5d66d0a60e6d4f38214"></a>

```c
#define SX1509B_GPIO_DEBOUNCE (1U << 8)
```

相关声明：[SX1509B_GPIO_DEBOUNCE](#a319917ebc030e5d66d0a60e6d4f38214)。

启用 GPIO 引脚去抖（Debounce）。

## 67.2\_详细说明（Detailed Documentation）

<a id="a319917ebc030e5d66d0a60e6d4f38214"></a>

### `SX1509B_GPIO_DEBOUNCE`

```c
#define SX1509B_GPIO_DEBOUNCE (1U << 8)
```

启用 GPIO 引脚去抖（Debounce）。

去抖标志（Debounce Flag）是 Zephyr 对 Linux GPIO 绑定所规定的标准 GPIO 标志的扩展。它仅适用于 Semtech SX1509B GPIO 控制器（Controllers）。


## 67.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P756_semtech-sx1509b.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P066_zephyr__drivers__disk__sdmmc_stm32.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P068_zephyr__drivers__sensor__sgp40.h_文件参考.md)
