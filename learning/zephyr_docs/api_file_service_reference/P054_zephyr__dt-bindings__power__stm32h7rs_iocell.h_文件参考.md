---
id: learning.zephyr-docs.api-file-service-reference.page-54
title: zephyr__dt-bindings__power__stm32h7rs_iocell.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32h7rs__iocell_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_zephyr\_\_dt-bindings\_\_power\_\_stm32h7rs\_iocell.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stm32h7rs__iocell_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STM32H7R/S设备的输入输出单元（I/O Cell）定义。

查看此文件的源码。

<a id="details"></a>

STM32H7R/S设备的输入输出单元（I/O Cell）定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 54.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 用于配置 STM32 I/O 单元设备的电源域（I/O Power Domains）

<a id="r_aa609f8dd3226eb0edb96200325f08f3b"></a>

```c
#define STM32_DT_IOCELL_VDDIO (0)
```

相关声明：[STM32_DT_IOCELL_VDDIO](#aa609f8dd3226eb0edb96200325f08f3b)。

由 VDD 电源（Supply）供电的输入输出域（I/O Domain）。

<a id="r_a9e9b4f4c10dca7f840fe026ab802b517"></a>

```c
#define STM32_DT_IOCELL_XSPI1 (1)
```

相关声明：[STM32_DT_IOCELL_XSPI1](#a9e9b4f4c10dca7f840fe026ab802b517)。

由 VDDXSPI1 电源（Supply）供电的输入输出域（I/O Domain）。

<a id="r_a108dc851abe5faf9d2c77f92d50966e4"></a>

```c
#define STM32_DT_IOCELL_XSPI2 (2)
```

相关声明：[STM32_DT_IOCELL_XSPI2](#a108dc851abe5faf9d2c77f92d50966e4)。

由 VDDXSPI2 电源（Supply）供电的输入输出域（I/O Domain）。

<a id="r_ad12edd016d0f8bb0603bdbbaf36b0e07"></a>

```c
#define STM32_DT_IOCELL_DOMAIN_VALID(domain)
```

相关声明：[STM32_DT_IOCELL_DOMAIN_VALID](#ad12edd016d0f8bb0603bdbbaf36b0e07)。

若该域是有效的输入输出域（I/O Domain），则返回 `true`。

## 54.2\_详细说明（Detailed Documentation）

<a id="ad12edd016d0f8bb0603bdbbaf36b0e07"></a>

### `STM32_DT_IOCELL_DOMAIN_VALID`

```c
#define STM32_DT_IOCELL_DOMAIN_VALID ( domain)
```

展开值（Value）：

```c
(((domain) >= 0) && ((domain) <= 2))
```

若该域是有效的输入输出域（I/O Domain），则返回 `true`。

<a id="aa609f8dd3226eb0edb96200325f08f3b"></a>

### `STM32_DT_IOCELL_VDDIO`

```c
#define STM32_DT_IOCELL_VDDIO (0)
```

由 VDD 电源（Supply）供电的输入输出域（I/O Domain）。

<a id="a9e9b4f4c10dca7f840fe026ab802b517"></a>

### `STM32_DT_IOCELL_XSPI1`

```c
#define STM32_DT_IOCELL_XSPI1 (1)
```

由 VDDXSPI1 电源（Supply）供电的输入输出域（I/O Domain）。

<a id="a108dc851abe5faf9d2c77f92d50966e4"></a>

### `STM32_DT_IOCELL_XSPI2`

```c
#define STM32_DT_IOCELL_XSPI2 (2)
```

由 VDDXSPI2 电源（Supply）供电的输入输出域（I/O Domain）。


## 54.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P836_stm32h7rs_iocell.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P053_zephyr__bluetooth__mesh__statistic.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P055_zephyr__dt-bindings__power__stm32n6_iocell.h_文件参考.md)
