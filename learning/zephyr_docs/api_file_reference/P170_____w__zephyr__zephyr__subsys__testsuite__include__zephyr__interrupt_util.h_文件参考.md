---
id: learning.zephyr-docs.api-file-reference.page-170
title: ____w__zephyr__zephyr__subsys__testsuite__include__zephyr__interrupt_util.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/interrupt__util_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第170章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_testsuite\_\_include\_\_zephyr\_\_interrupt\_util.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/interrupt__util_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 170.1\_宏定义（Macros）

<a id="r_a48fcf2be56c2b4cb0fb15d77c9194f89"></a>

```c
#define k_str_out_count(s)
```

相关声明：[k_str_out_count](#a48fcf2be56c2b4cb0fb15d77c9194f89)。

<a id="r_a3bef33fb908a7ffd30a3f9b433dacf18"></a>

```c
#define NO_TRIGGER_FROM_SW
```

相关声明：[NO_TRIGGER_FROM_SW](#a3bef33fb908a7ffd30a3f9b433dacf18)。

## 170.2\_详细说明（Detailed Documentation）

<a id="a48fcf2be56c2b4cb0fb15d77c9194f89"></a>

### `k_str_out_count`

```c
#define k_str_out_count ( s)
```

展开值（Value）：

```c
k_str_out((s), sizeof(s) - 1);
```

<a id="a3bef33fb908a7ffd30a3f9b433dacf18"></a>

### `NO_TRIGGER_FROM_SW`

```c
#define NO_TRIGGER_FROM_SW
```


## 170.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/interrupt__util_8h_source.html)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P169_zephyr__dt-bindings__reset__intel_socfpga_reset.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P171_____w__zephyr__zephyr__lib__libc__minimal__include__inttypes.h_文件参考.md)
