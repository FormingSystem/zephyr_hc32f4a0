---
id: learning.zephyr-docs.api-file-reference.page-146
title: zephyr__dt-bindings__clock__ifx_clock_source_psoc4xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__psoc4xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第146章\_zephyr\_\_dt-bindings\_\_clock\_\_ifx\_clock\_source\_psoc4xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__psoc4xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 146.1\_宏定义（Macros）

<a id="r_a68b9ddcd8f5178a83de6c4fee5411224"></a>

```c
#define IFX_PATH_PSOC4_IMO 0
```

相关声明：[IFX_PATH_PSOC4_IMO](#a68b9ddcd8f5178a83de6c4fee5411224)。

<a id="r_a0aa92d92989c4f26c35dd6a3fdf4ac02"></a>

```c
#define IFX_PATH_PSOC4_EXT 1
```

相关声明：[IFX_PATH_PSOC4_EXT](#a0aa92d92989c4f26c35dd6a3fdf4ac02)。

<a id="r_ab22636fa0990e9d297d1e2b03e3ecb27"></a>

```c
#define IFX_PATH_PSOC4_PUMP_GND 0
```

相关声明：[IFX_PATH_PSOC4_PUMP_GND](#ab22636fa0990e9d297d1e2b03e3ecb27)。

<a id="r_aa3d7b7c00d0969721efce8fa275d29de"></a>

```c
#define IFX_PATH_PSOC4_PUMP_IMO 1
```

相关声明：[IFX_PATH_PSOC4_PUMP_IMO](#aa3d7b7c00d0969721efce8fa275d29de)。

<a id="r_a07024ea9ded094c2f90616caafba6dde"></a>

```c
#define IFX_PATH_PSOC4_PUMP_HFCLK 2
```

相关声明：[IFX_PATH_PSOC4_PUMP_HFCLK](#a07024ea9ded094c2f90616caafba6dde)。

<a id="r_a942d2c611b1c466a71408a66cd327671"></a>

```c
#define IFX_PSOC4_HFCLK_DIV(div)
```

相关声明：[IFX_PSOC4_HFCLK_DIV](#a942d2c611b1c466a71408a66cd327671)。

## 146.2\_详细说明（Detailed Documentation）

<a id="a0aa92d92989c4f26c35dd6a3fdf4ac02"></a>

### `IFX_PATH_PSOC4_EXT`

```c
#define IFX_PATH_PSOC4_EXT 1
```

<a id="a68b9ddcd8f5178a83de6c4fee5411224"></a>

### `IFX_PATH_PSOC4_IMO`

```c
#define IFX_PATH_PSOC4_IMO 0
```

<a id="ab22636fa0990e9d297d1e2b03e3ecb27"></a>

### `IFX_PATH_PSOC4_PUMP_GND`

```c
#define IFX_PATH_PSOC4_PUMP_GND 0
```

<a id="a07024ea9ded094c2f90616caafba6dde"></a>

### `IFX_PATH_PSOC4_PUMP_HFCLK`

```c
#define IFX_PATH_PSOC4_PUMP_HFCLK 2
```

<a id="aa3d7b7c00d0969721efce8fa275d29de"></a>

### `IFX_PATH_PSOC4_PUMP_IMO`

```c
#define IFX_PATH_PSOC4_PUMP_IMO 1
```

<a id="a942d2c611b1c466a71408a66cd327671"></a>

### `IFX_PSOC4_HFCLK_DIV`

```c
#define IFX_PSOC4_HFCLK_DIV ( div)
```

展开值（Value）：

```c
((div) == 0   ? CY_SYSCLK_NO_DIV                                                           \
 : (div) == 1 ? CY_SYSCLK_DIV_2                                                            \
 : (div) == 3 ? CY_SYSCLK_DIV_4                                                            \
 : (div) == 7 ? CY_SYSCLK_DIV_8                                                            \
              : CY_SYSCLK_NO_DIV)
```


## 146.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_runtime_reference/P032_ifx_clock_source_psoc4xx.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P145_zephyr__dt-bindings__clock__ifx_clock_source_pse8xx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P147_zephyr__dt-bindings__misc__ifx_cyw20829.h_文件参考.md)
