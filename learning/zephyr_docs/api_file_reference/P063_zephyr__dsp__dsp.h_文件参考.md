---
id: learning.zephyr-docs.api-file-reference.page-63
title: zephyr__dsp__dsp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dsp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_zephyr\_\_dsp\_\_dsp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dsp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数字信号处理（Digital Signal Processing，DSP）数学运算的公共API。

<a id="details"></a>

```c
#include <zephyr/dsp/types.h>
#include <zephyr/dsp/basicmath.h>
#include <zephyr/dsp/print_format.h>
#include "zdsp_backend.h"
```

查看此文件的源码。

数字信号处理（Digital Signal Processing，DSP）数学运算的公共API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 63.1\_宏定义（Macros）

<a id="r_a88feaebec50a9dcd42836439a9849bc7"></a>

```c
#define DSP_FUNC_SCOPE
```

相关声明：[DSP_FUNC_SCOPE](#a88feaebec50a9dcd42836439a9849bc7)。

<a id="r_a2ba5cab25d6c097e55bbe14094a06c7c"></a>

```c
#define DSP_DATA
```

相关声明：[DSP_DATA](#a2ba5cab25d6c097e55bbe14094a06c7c)。

<a id="r_aab42290c42efbdc1d93c5530da099911"></a>

```c
#define DSP_STATIC_DATA DSP_DATA
```

相关声明：[DSP_STATIC_DATA](#aab42290c42efbdc1d93c5530da099911)、[DSP_DATA](#a2ba5cab25d6c097e55bbe14094a06c7c)。

## 63.2\_详细说明（Detailed Documentation）

<a id="a2ba5cab25d6c097e55bbe14094a06c7c"></a>

### `DSP_DATA`

```c
#define DSP_DATA
```

<a id="a88feaebec50a9dcd42836439a9849bc7"></a>

### `DSP_FUNC_SCOPE`

```c
#define DSP_FUNC_SCOPE
```

<a id="aab42290c42efbdc1d93c5530da099911"></a>

### `DSP_STATIC_DATA`

```c
#define DSP_STATIC_DATA DSP_DATA
```


## 63.3\_原页交叉引用（Cross References）

- [zephyr/dsp/types.h](../api_source_reference/P364_types.h_源码浏览.md)
- [zephyr/dsp/basicmath.h](../api_source_reference/P053_basicmath.h_源码浏览.md)
- [zephyr/dsp/print_format.h](../api_source_reference/P670_print_format.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P187_dsp.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P062_zephyr__dt-bindings__ethernet__dsa_tag_proto.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P064_zephyr__dt-bindings__acpi__acpi.h_文件参考.md)
