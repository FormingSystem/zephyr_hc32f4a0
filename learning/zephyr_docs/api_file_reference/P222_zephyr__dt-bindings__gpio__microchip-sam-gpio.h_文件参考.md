---
id: learning.zephyr-docs.api-file-reference.page-222
title: zephyr__dt-bindings__gpio__microchip-sam-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/microchip-sam-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第222章\_zephyr\_\_dt-bindings\_\_gpio\_\_microchip-sam-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/microchip-sam-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 222.1\_宏定义（Macros）

<a id="r_aa4c1e0977632472721aa08d4138d7816"></a>

```c
#define SAM_GPIO_DIS_SLEWRATE (1U << 8)
```

相关声明：[SAM_GPIO_DIS_SLEWRATE](#aa4c1e0977632472721aa08d4138d7816)。

<a id="r_a0747d762ffd1e5e91ac15baacb7680d7"></a>

```c
#define SAM_GPIO_DEBOUNCE (1U << 9)
```

相关声明：[SAM_GPIO_DEBOUNCE](#a0747d762ffd1e5e91ac15baacb7680d7)。

<a id="r_afe7c3a9935a0696b8236ba634311483d"></a>

```c
#define SAM_GPIO_DIS_SCHMIT (1U << 10)
```

相关声明：[SAM_GPIO_DIS_SCHMIT](#afe7c3a9935a0696b8236ba634311483d)。

<a id="r_af78ea1c81e382ca9b56fcb10ea011e5c"></a>

```c
#define SAM_GPIO_DRVSTR_POS (11U)
```

相关声明：[SAM_GPIO_DRVSTR_POS](#af78ea1c81e382ca9b56fcb10ea011e5c)。

<a id="r_a7126253bbd005f80cf0481fb61442dc1"></a>

```c
#define SAM_GPIO_DRVSTR_MASK (0x3U << SAM_GPIO_DRVSTR_POS)
```

相关声明：[SAM_GPIO_DRVSTR_MASK](#a7126253bbd005f80cf0481fb61442dc1)、[SAM_GPIO_DRVSTR_POS](#af78ea1c81e382ca9b56fcb10ea011e5c)。

<a id="r_a6ccfb90808dddb69d62591e9e2878609"></a>

```c
#define SAM_GPIO_DRVSTR_DEFAULT (0U << SAM_GPIO_DRVSTR_POS)
```

相关声明：[SAM_GPIO_DRVSTR_DEFAULT](#a6ccfb90808dddb69d62591e9e2878609)、[SAM_GPIO_DRVSTR_POS](#af78ea1c81e382ca9b56fcb10ea011e5c)。

<a id="r_a0ed57b2d5539642d3269da76b6133935"></a>

```c
#define SAM_GPIO_DRVSTR_LOW (1U << SAM_GPIO_DRVSTR_POS)
```

相关声明：[SAM_GPIO_DRVSTR_LOW](#a0ed57b2d5539642d3269da76b6133935)、[SAM_GPIO_DRVSTR_POS](#af78ea1c81e382ca9b56fcb10ea011e5c)。

<a id="r_af5c9c59a909406e3a312a2be4f5a0072"></a>

```c
#define SAM_GPIO_DRVSTR_MED (2U << SAM_GPIO_DRVSTR_POS)
```

相关声明：[SAM_GPIO_DRVSTR_MED](#af5c9c59a909406e3a312a2be4f5a0072)、[SAM_GPIO_DRVSTR_POS](#af78ea1c81e382ca9b56fcb10ea011e5c)。

<a id="r_a0d053d2914b317f08bbd3d322e6718f3"></a>

```c
#define SAM_GPIO_DRVSTR_HI (3U << SAM_GPIO_DRVSTR_POS)
```

相关声明：[SAM_GPIO_DRVSTR_HI](#a0d053d2914b317f08bbd3d322e6718f3)、[SAM_GPIO_DRVSTR_POS](#af78ea1c81e382ca9b56fcb10ea011e5c)。

## 222.2\_详细说明（Detailed Documentation）

<a id="a0747d762ffd1e5e91ac15baacb7680d7"></a>

### `SAM_GPIO_DEBOUNCE`

```c
#define SAM_GPIO_DEBOUNCE (1U << 9)
```

<a id="afe7c3a9935a0696b8236ba634311483d"></a>

### `SAM_GPIO_DIS_SCHMIT`

```c
#define SAM_GPIO_DIS_SCHMIT (1U << 10)
```

<a id="aa4c1e0977632472721aa08d4138d7816"></a>

### `SAM_GPIO_DIS_SLEWRATE`

```c
#define SAM_GPIO_DIS_SLEWRATE (1U << 8)
```

<a id="a6ccfb90808dddb69d62591e9e2878609"></a>

### `SAM_GPIO_DRVSTR_DEFAULT`

```c
#define SAM_GPIO_DRVSTR_DEFAULT (0U << SAM_GPIO_DRVSTR_POS)
```

<a id="a0d053d2914b317f08bbd3d322e6718f3"></a>

### `SAM_GPIO_DRVSTR_HI`

```c
#define SAM_GPIO_DRVSTR_HI (3U << SAM_GPIO_DRVSTR_POS)
```

<a id="a0ed57b2d5539642d3269da76b6133935"></a>

### `SAM_GPIO_DRVSTR_LOW`

```c
#define SAM_GPIO_DRVSTR_LOW (1U << SAM_GPIO_DRVSTR_POS)
```

<a id="a7126253bbd005f80cf0481fb61442dc1"></a>

### `SAM_GPIO_DRVSTR_MASK`

```c
#define SAM_GPIO_DRVSTR_MASK (0x3U << SAM_GPIO_DRVSTR_POS)
```

<a id="af5c9c59a909406e3a312a2be4f5a0072"></a>

### `SAM_GPIO_DRVSTR_MED`

```c
#define SAM_GPIO_DRVSTR_MED (2U << SAM_GPIO_DRVSTR_POS)
```

<a id="af78ea1c81e382ca9b56fcb10ea011e5c"></a>

### `SAM_GPIO_DRVSTR_POS`

```c
#define SAM_GPIO_DRVSTR_POS (11U)
```


## 222.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/microchip-sam-gpio_8h_source.html)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P221_zephyr__drivers__mic_privacy__intel__mic_privacy.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P223_zephyr__dt-bindings__interrupt-controller__microchip-smartfusion2-irq.h_文件参考.md)
