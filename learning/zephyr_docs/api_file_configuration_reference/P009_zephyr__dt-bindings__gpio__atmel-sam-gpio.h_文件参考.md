---
id: learning.zephyr-docs.api-file-configuration-reference.page-9
title: zephyr__dt-bindings__gpio__atmel-sam-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/atmel-sam-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_dt-bindings\_\_gpio\_\_atmel-sam-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/atmel-sam-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.1\_宏定义（Macros）

<a id="r_a0747d762ffd1e5e91ac15baacb7680d7"></a>

```c
#define SAM_GPIO_DEBOUNCE (1U << 8)
```

相关声明：[SAM_GPIO_DEBOUNCE](#a0747d762ffd1e5e91ac15baacb7680d7)。

启用 GPIO 引脚去抖（Debounce）。

## 9.2\_详细说明（Detailed Documentation）

<a id="a0747d762ffd1e5e91ac15baacb7680d7"></a>

### `SAM_GPIO_DEBOUNCE`

```c
#define SAM_GPIO_DEBOUNCE (1U << 8)
```

启用 GPIO 引脚去抖（Debounce）。

去抖标志（Debounce Flag）是 Zephyr 对 Linux GPIO 绑定所规定的标准 GPIO 标志的扩展。它仅适用于 Atmel SAM 片上系统（SoCs）。


## 9.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P043_atmel-sam-gpio.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P008_zephyr__drivers__clock_control__arm_clock_control.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__dt-bindings__dma__atmel_samx7x_dma.h_文件参考.md)
