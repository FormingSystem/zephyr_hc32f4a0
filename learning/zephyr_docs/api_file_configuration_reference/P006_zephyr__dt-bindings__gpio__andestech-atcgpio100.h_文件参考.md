---
id: learning.zephyr-docs.api-file-configuration-reference.page-6
title: zephyr__dt-bindings__gpio__andestech-atcgpio100.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/andestech-atcgpio100_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_dt-bindings\_\_gpio\_\_andestech-atcgpio100.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/andestech-atcgpio100_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_ac2da1c070a96a2aa921035f21a6aff21"></a>

```c
#define ATCGPIO100_GPIO_DEBOUNCE (1U << 8)
```

相关声明：[ATCGPIO100_GPIO_DEBOUNCE](#ac2da1c070a96a2aa921035f21a6aff21)。

启用 GPIO 引脚去抖（Debounce）。

## 6.2\_详细说明（Detailed Documentation）

<a id="ac2da1c070a96a2aa921035f21a6aff21"></a>

### `ATCGPIO100_GPIO_DEBOUNCE`

```c
#define ATCGPIO100_GPIO_DEBOUNCE (1U << 8)
```

启用 GPIO 引脚去抖（Debounce）。

去抖标志（Debounce Flag）是 Zephyr 对 Linux GPIO 绑定所规定的标准 GPIO 标志的扩展。它仅适用于 Andestech Technology Corporation ATCGPIO100 片上系统（SoCs）。


## 6.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P031_andestech-atcgpio100.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P005_zephyr__drivers__flash__andes_flash_xip_api_ex.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__sensor__apds9960.h_文件参考.md)
