---
id: learning.zephyr-docs.api-file-interface-reference.page-46
title: zephyr__dt-bindings__gpio__realtek-bee-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/realtek-bee-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_zephyr\_\_dt-bindings\_\_gpio\_\_realtek-bee-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/realtek-bee-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Realtek Bee GPIO控制器（Controller）的专用定义。

查看此文件的源码。

<a id="details"></a>

Realtek Bee GPIO 控制器专用定义。本文件包含 Realtek Bee 系列片上系统（SoC）专用的 GPIO 配置标志，供设备树绑定（Device Tree bindings）使用。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 46.1\_宏定义（Macros）

<a id="r_ac78d9506eb59cb5c5da439bfd178df62"></a>

```c
#define BEE_GPIO_INPUT_DEBOUNCE_MS(ms)
```

相关声明：[BEE_GPIO_INPUT_DEBOUNCE_MS](#ac78d9506eb59cb5c5da439bfd178df62)。

启用 GPIO 引脚去抖（Debounce）。

<a id="define-members-0"></a>

### GPIO 去抖配置（Debounce Configuration）

<a id="r_a1e0512581a5de61d40272df5a5a2ffe6"></a>

```c
#define BEE_GPIO_INPUT_DEBOUNCE_MS_POS 8
```

相关声明：[BEE_GPIO_INPUT_DEBOUNCE_MS_POS](#a1e0512581a5de61d40272df5a5a2ffe6)。

去抖时间（debounce time）的位位置，时间单位为毫秒。

<a id="r_a5baefbab48945fbfc41240b5fcac034e"></a>

```c
#define BEE_GPIO_INPUT_DEBOUNCE_MS_MASK (0xff << BEE_GPIO_INPUT_DEBOUNCE_MS_POS)
```

相关声明：[BEE_GPIO_INPUT_DEBOUNCE_MS_MASK](#a5baefbab48945fbfc41240b5fcac034e)、[BEE_GPIO_INPUT_DEBOUNCE_MS_POS](#a1e0512581a5de61d40272df5a5a2ffe6)。

去抖时间配置的位掩码（bit mask）。

## 46.2\_详细说明（Detailed Documentation）

<a id="ac78d9506eb59cb5c5da439bfd178df62"></a>

### `BEE_GPIO_INPUT_DEBOUNCE_MS`

```c
#define BEE_GPIO_INPUT_DEBOUNCE_MS ( ms)
```

展开值（Value）：

```c
((0xff & (ms)) << BEE_GPIO_INPUT_DEBOUNCE_MS_POS)
```

启用 GPIO 引脚去抖（Debounce）。

去抖标志（debounce flag）是 Zephyr 对 Linux GPIO 绑定所规定标准 GPIO 标志的专用扩展。仅适用于 Realtek Bee SoC。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ms` | 去抖时间，单位为毫秒，取值为 0–255。 |

<a id="a5baefbab48945fbfc41240b5fcac034e"></a>

### `BEE_GPIO_INPUT_DEBOUNCE_MS_MASK`

```c
#define BEE_GPIO_INPUT_DEBOUNCE_MS_MASK (0xff << BEE_GPIO_INPUT_DEBOUNCE_MS_POS)
```

去抖时间配置的位掩码（bit mask）。

<a id="a1e0512581a5de61d40272df5a5a2ffe6"></a>

### `BEE_GPIO_INPUT_DEBOUNCE_MS_POS`

```c
#define BEE_GPIO_INPUT_DEBOUNCE_MS_POS 8
```

去抖时间（debounce time）的位位置，时间单位为毫秒。


## 46.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P697_realtek-bee-gpio.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="arealtek-bee-gpio_8h_html_a1e0512581a5de61d40272df5a5a2ffe6"></a>

---

[上一章](P045_zephyr__dt-bindings__clock__ra_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P047_zephyr__xen__regions.h_文件参考.md)
