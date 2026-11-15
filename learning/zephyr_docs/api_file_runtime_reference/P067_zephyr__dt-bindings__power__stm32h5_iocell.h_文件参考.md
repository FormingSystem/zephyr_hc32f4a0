---
id: learning.zephyr-docs.api-file-runtime-reference.page-67
title: zephyr__dt-bindings__power__stm32h5_iocell.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32h5__iocell_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_zephyr\_\_dt-bindings\_\_power\_\_stm32h5\_iocell.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stm32h5__iocell_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STM32H5设备的输入输出单元（I/O Cell）定义。

查看此文件的源码。

<a id="details"></a>

STM32H5设备的输入输出单元（I/O Cell）定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 67.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 用于配置 STM32H5 I/O 单元设备的电源域（I/O Power Domains）

<a id="r_aa609f8dd3226eb0edb96200325f08f3b"></a>

```c
#define STM32_DT_IOCELL_VDDIO (0)
```

相关声明：[STM32_DT_IOCELL_VDDIO](#aa609f8dd3226eb0edb96200325f08f3b)。

由 VDD 电源（Supply）供电的输入输出域（I/O Domain）。

<a id="r_adcb79a3c0f4b1aefbeeb56a1da714a5d"></a>

```c
#define STM32_DT_IOCELL_VDDIO2 (1)
```

相关声明：[STM32_DT_IOCELL_VDDIO2](#adcb79a3c0f4b1aefbeeb56a1da714a5d)。

由 VDDIO2 电源（Supply）供电的输入输出域（I/O Domain）。

<a id="r_ad12edd016d0f8bb0603bdbbaf36b0e07"></a>

```c
#define STM32_DT_IOCELL_DOMAIN_VALID(domain)
```

相关声明：[STM32_DT_IOCELL_DOMAIN_VALID](#ad12edd016d0f8bb0603bdbbaf36b0e07)。

若该域是有效的输入输出域（I/O Domain），则返回 `true`。

## 67.2\_详细说明（Detailed Documentation）

<a id="ad12edd016d0f8bb0603bdbbaf36b0e07"></a>

### `STM32_DT_IOCELL_DOMAIN_VALID`

```c
#define STM32_DT_IOCELL_DOMAIN_VALID ( domain)
```

展开值（Value）：

```c
(((domain) >= 0) && ((domain) <= 1))
```

若该域是有效的输入输出域（I/O Domain），则返回 `true`。

<a id="aa609f8dd3226eb0edb96200325f08f3b"></a>

### `STM32_DT_IOCELL_VDDIO`

```c
#define STM32_DT_IOCELL_VDDIO (0)
```

由 VDD 电源（Supply）供电的输入输出域（I/O Domain）。

<a id="adcb79a3c0f4b1aefbeeb56a1da714a5d"></a>

### `STM32_DT_IOCELL_VDDIO2`

```c
#define STM32_DT_IOCELL_VDDIO2 (1)
```

由 VDDIO2 电源（Supply）供电的输入输出域（I/O Domain）。


## 67.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P835_stm32h5_iocell.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P066_zephyr__dt-bindings__power__stm32_pwr.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P068_zephyr__net__prometheus__summary.h_文件参考.md)
